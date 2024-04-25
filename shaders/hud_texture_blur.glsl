#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec2 in_texcoord_0;
out vec2 uv0;

void main() {
    gl_Position = vec4(in_position, 1);
    uv0 = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

out vec4 fragColor;
uniform sampler2D texture0;
uniform sampler2D texture1;
in vec2 uv0;
uniform vec2 screen_size;
uniform float Quality;
uniform float Directions;

const float Pi = 3.14159265359;
const int blur_size = 16; //16

vec4 layer(vec4 foreground, vec4 background) {
    return foreground * foreground.a + background * (1.0 - foreground.a);
}

vec4 compute_blur(in float a) {
    if (a > 0) {
        if (a == 1) {
            return texture(texture1, uv0);
        }
        // GAUSSIAN BLUR SETTINGS {{{
        // BLUR DIRECTIONS (Default 16.0 - More is better but slower)
        // BLUR QUALITY (Default 4.0 - More is better but slower)
        // GAUSSIAN BLUR SETTINGS }}}

        vec2 Radius = blur_size/screen_size;

        // Normalized pixel coordinates (from 0 to 1)
        vec2 uv = uv0/screen_size;
        // Pixel colour
        vec4 Color = texture(texture1, uv0);

        // Blur calculations
        for (float d=0.0; d<Pi; d+=Pi/Directions) {
            for (float i=1.0/Quality; i<=1.0; i+=1.0/Quality) {
                Color += texture(texture1, uv0+vec2(cos(d), sin(d))*Radius*i);
            }
        }

        // Output to screen
        Color /= Quality * Directions;
        return Color;
    }
    if (a == 0) return texture(texture1, uv0);
}

void main() {
    vec4 foreground = texture(texture0, vec2(uv0.x, -uv0.y)).bgra;
    //vec4 background = texture(texture1, vec2(uv0.x, -uv0.y)).bgra

    fragColor = layer(foreground, compute_blur(foreground.a).bgra);
}
#endif
