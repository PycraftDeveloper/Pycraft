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

vec4 layer(vec4 foreground, vec4 background) {
    return foreground * foreground.a + background * (1.0 - foreground.a);
}

void main() {
    vec4 foreground = texture(texture0, vec2(uv0.x, -uv0.y)).bgra;
    vec4 background = texture(texture1, uv0).bgra;

    fragColor = layer(foreground, background);
}

#endif
