#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec2 in_texcoord_0;

uniform mat4 m_model;
uniform mat4 m_camera;
uniform mat4 m_proj;

out vec4 mVertex;
out vec2 ppos;
out vec2 uv0;

void main() {
    mat4 m_view = m_camera * m_model;
    vec4 p = m_view * vec4(in_position.xzy, 1.0);
    vec4 position =  m_proj * p;
    gl_Position = position;

    mVertex = gl_Position;
    uv0 = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

in vec4 mVertex;
in vec2 uv0;

uniform vec4 CameraEye;
uniform bool render_fog;
uniform float w_min;
uniform float w_max;
uniform vec2 camera_pos;
uniform float cloud_scale;

out vec4 fragColor;

#define PI 3.1415926535897932384626433832795;

float rand(vec2 c) {
	return fract(sin(dot(c.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

float noise(vec2 p, float freq){
	float unit = 1/freq;
	vec2 ij = floor(p/unit);
	vec2 xy = mod(p,unit)/unit;
	xy = 3.*xy*xy-2.*xy*xy*xy;
	//xy = 0.5*(1.-cos(PI*xy));
	float a = rand((ij+vec2(0.,0.)));
	float b = rand((ij+vec2(1.,0.)));
	float c = rand((ij+vec2(0.,1.)));
	float d = rand((ij+vec2(1.,1.)));
	float x1 = mix(a, b, xy.x);
	float x2 = mix(c, d, xy.x);
	return mix(x1, x2, xy.y);
}

float pNoise(vec2 p, int res){
	float persistance = .5;
	float n = 0.;
	float normK = 0.;
	float f = 4.;
	float amp = 1.;
	int iCount = 0;
	for (int i = 0; i<50; i++){
		n+=amp*noise(p, f);
		f*=2.;
		normK+=amp;
		amp*=persistance;
		if (iCount == res) break;
		iCount++;
	}
	float nf = n/normK;
	return nf*nf*nf*nf;
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
    vec4 V = mVertex;
    float d = distance(CameraEye, V);
    float alpha = getFogFactor(d, w_max, w_min);
    float lum = 1-noise(camera_pos+uv0*cloud_scale, 1);
    if (lum == 1) discard;
    fragColor = vec4(1-lum/20, 1-lum/20, 1-lum/20, (1.0-alpha)*lum);
}
#endif