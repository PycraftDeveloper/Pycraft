#version 330

#if defined VERTEX_SHADER

uniform mat4 projection;

in vec2 in_pos;
in vec3 in_color;
out vec3 color;

void main() {
    gl_Position = projection * vec4(in_pos, 1.0, 1.0);
    color = in_color;
}

#elif defined FRAGMENT_SHADER

out vec4 f_color;
in vec3 color;

void main() {
    f_color = vec4(color, 1.0);
}

#endif