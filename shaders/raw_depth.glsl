#version 330
#if defined VERTEX_SHADER

uniform mat4 u_mvp;

in vec3 in_position;

void main() {
    gl_Position = u_mvp * vec4(in_position, 1.0);
}

#elif defined FRAGMENT_SHADER

void main() {
}
#endif