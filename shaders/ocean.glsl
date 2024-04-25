#version 330

#if defined VERTEX_SHADER

in vec3 in_position;

uniform mat4 m_model;
uniform mat4 m_camera;
uniform mat4 m_proj;

out vec4 mVertex;

void main() {
    mat4 m_view = m_camera * m_model;
    vec4 p = m_view * vec4(in_position.xzy, 1.0);
    vec4 position =  m_proj * p;
    gl_Position = position;

    mVertex = gl_Position;
}

#elif defined FRAGMENT_SHADER

in vec4 mVertex;

uniform vec4 CameraEye;
uniform bool render_fog;
uniform float w_min;
uniform float w_max;

out vec4 fragColor;

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
    vec4 V = mVertex;
    float d = distance(CameraEye, V);
    float alpha = getFogFactor(d, w_max, w_min);
    fragColor = vec4(0.043137, 0.682353, 0.709804, 1-alpha).bgra;
}
#endif