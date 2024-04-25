#version 330

#if defined VERTEX_SHADER

in vec3 in_normal;
in vec3 in_position;
in vec2 in_texcoord_0;
in vec3 in_color;

uniform mat4 bias_matrix;
uniform mat4 mvp_light;
uniform mat4 projection_matrix;
uniform mat4 matrix;
uniform float w_max;

out vec4 mVertex;
out vec3 v_norm;
out vec4 v_shadow_coord;
out vec2 v_text;
out vec3 v_vert;
out float m;

void main() {
    mat4 u_mvp = projection_matrix * matrix;
    vec4 position = u_mvp * vec4(in_position, 1.0);
    gl_Position = position;

    m = in_normal.y;

    mat4 u_depth_bias_mvp = bias_matrix * mvp_light;
    v_shadow_coord = u_depth_bias_mvp * vec4(in_position, 1.0);

    v_vert = in_position;
    v_norm = in_normal;
    v_text = in_texcoord_0;

    mVertex = position;
}

#elif defined FRAGMENT_SHADER

in vec4 mVertex;
in vec3 v_norm;
in vec4 v_shadow_coord;
in vec2 v_text;
in vec3 v_vert;
in float m;

uniform vec4 CameraEye;
uniform vec4 FogColor;
uniform float light_level;
uniform vec3 u_color;
uniform vec3 u_light;
uniform float w_max;

uniform sampler2D grass_color;
uniform sampler2D rock_color;

uniform sampler2DShadow u_sampler_shadow;
uniform bool u_use_color_texture;
uniform float w_min;
uniform bool render_fog;
uniform vec2 repeat = vec2(2, 2);
out vec4 f_color;

float compute_visibility(in float cos_theta) {
    // shadow coordinates in light space
    vec2 shadow_coord_ls = v_shadow_coord.xy / v_shadow_coord.w;

    // bias according to the slope
    float bias = 0.005 * tan(acos(cos_theta));
    bias = clamp(bias, 0.0, 0.01);

    float z_from_cam = v_shadow_coord.z / v_shadow_coord.w - bias;
    vec3 shadow_coord = vec3(shadow_coord_ls, z_from_cam);
    float shadow_value = texture(u_sampler_shadow, shadow_coord);
    return 1.0 - shadow_value;
}

float getFogFactor(float d, float w_max, float w_min)
{
        if (d >= w_max) discard;
        if (d <= w_min) return 0.0;

    if (render_fog == true) {
        return 1.0-(w_max - d) / (w_max - w_min);
    } else {
        return 0.0;
    }
}

void main() {
    // Lighting
    // Diffuse lighting + ambient
    vec4 V = mVertex;
    float d = distance(CameraEye, V);
    float alpha = getFogFactor(d, w_max, w_min);

    vec3 light_vector_obj_space = normalize(u_light - v_vert);
    vec3 normal_obj_space = normalize(v_norm);
    float cos_theta = dot(light_vector_obj_space, normal_obj_space);
    float diffuse = clamp(cos_theta, 0.0, 1.0);
    // Shadow component
    float lum = mix(light_level, 1.0, diffuse * compute_visibility(cos_theta));

    vec3 grass_texture = texture2D(grass_color, vec2(mod(v_text.x * repeat.x, 1.0), mod(v_text.y * repeat.y, 1.0))).bgr;
    vec3 rock_texture = texture2D(rock_color, vec2(mod(v_text.x * repeat.x, 1.0), mod(v_text.y * repeat.y, 1.0))).bgr;

    vec3 shaded_grass_texture = vec3(grass_texture);
    vec3 shaded_rock_texture = vec3(rock_texture);

    vec3 shaded_texture = vec3(mix(shaded_grass_texture, shaded_rock_texture, 1.0-m));
    // Final pixel color

    f_color = vec4(((shaded_texture.rgb)*u_color)*lum, 1.0-alpha);
}
#endif