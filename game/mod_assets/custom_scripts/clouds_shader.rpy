init python:

    #Credit to murieron for making the original shader (https://cineshader.com/view/WdXBW4)
    renpy.register_shader("shaders.clouds",
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;
            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;

            uniform float u_speed;
            uniform float u_cloud_scale;
            uniform float u_cloud_cover;
            uniform float u_cloud_alpha;
            uniform vec3 u_cloud_color;
            uniform vec3 u_sky_color_top;
            uniform vec3 u_sky_color_bottom;
            uniform float u_wind_direction;

        """,
        fragment_functions="""
            const mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
            vec2 hash(vec2 p){
                p = vec2(dot(p, vec2(184.1, 371.7)), dot(p, vec2(296.52, 193.3)));
                return -1. + 2. * fract(sin(p) * 81735.173851);
            }

            float noise(vec2 p){
                const float K1 = 0.366025404;
                const float K2 = 0.211324865;
                vec2 i = floor(p + (p.x+p.y)*K1);	
                vec2 a = p - i + (i.x+i.y)*K2;
                vec2 o = vec2(.0);
                if(a.x>a.y)
                    o = vec2(1.0,0.0);
                
                else 
                    o = vec2(0.0,1.0);

                vec2 b = a - o + K2;
                vec2 c = a - 1.0 + 2.0*K2;
                vec3 h = max(0.5-vec3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );
                vec3 n = h*h*h*h*vec3( dot(a,hash(i+0.0)), dot(b,hash(i+o)), dot(c,hash(i+1.0)));
                return dot(n, vec3(70.0));	
            }

            float fbm(vec2 n){
                float total = 0., amplitude = .1;
                for(int i = 0; i < 7; i++){
                    total += noise(n) * amplitude;
                    n *= m;
                    amplitude *= .4;
                }
                return total;
            }
        """,
        vertex_200="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_200="""
            const mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
            vec2 windDirection = vec2(u_wind_direction, 0.);

            vec2 p = (v_tex_coord * u_model_size) / u_model_size;
            vec2 base_uv = p * vec2(u_model_size.x / u_model_size.y, 1.0);

            float time = u_time * u_speed;

            float q = fbm(base_uv * u_cloud_scale * 0.5);

            // ridge noise shape
            float r = 0.0;
            vec2 uv = base_uv * u_cloud_scale;
            uv -= q - time * windDirection;
            float weight = 0.8;
            for (int i = 0; i < 8; i++) {
                r += abs(weight * noise(uv));
                uv = m * uv + time;
                weight *= 0.7;
            }

            // shape noise
            float f = 0.0;
            uv = base_uv * u_cloud_scale;
            uv -= q - time * windDirection;
            weight = 0.7;
            for (int i = 0; i < 8; i++) {
                f += weight * noise(uv);
                uv = m * uv + time;
                weight *= 0.6;
            }

            f *= r + f;

            // color noise
            float c = 0.0;
            time = u_time * u_speed * 2.0;
            uv = base_uv * u_cloud_scale * 2.0;
            uv -= q - time * windDirection;
            weight = 0.4;
            for (int i = 0; i < 7; i++) {
                c += weight * noise(uv);
                uv = m * uv + time;
                weight *= 0.6;
            }

            // ridge color noise
            float c1 = 0.0;
            time = u_time * u_speed * 3.0;
            uv = base_uv * u_cloud_scale * 3.0;
            uv -= q - time * windDirection;
            weight = 0.4;
            for (int i = 0; i < 7; i++) {
                c1 += abs(weight * noise(uv));
                uv = m * uv + time;
                weight *= 0.6;
            }

            c += c1;

            vec3 sky_color = mix(u_sky_color_bottom, u_sky_color_top, p.y);
            vec3 cloud_color = u_cloud_color * u_cloud_alpha;
        
            f = u_cloud_cover + u_cloud_alpha * f * r;
            
            vec3 result = mix(sky_color, clamp(sky_color + cloud_color, 0.0, 1.0), clamp(f + c, 0.0, 1.0));
            
            gl_FragColor = vec4( result, 1.0 );
        """)


    #Hover the 'Clouds' word below to display the documentation in VSCode.
    class Clouds(renpy.Displayable):
        """
        This class generates a sky filled with animated clouds. As always, usage is
        pretty easy, defining an image using this class and its parameters:
            `image clouds = Clouds(parameters)`
        
        Finding the parameters values you actually need/want relies heavily on trial,
        but 90% of the possible configurations will always look correct. In any case,
        don't hesitate to DM me on Discord for extra info (iitzwolfyy_).

        Parameters are the following:

        - `speed`: The speed of the clouds. If 0, clouds don't move. On the other hand,
        if it's higher than 0.5, they are extremely fast, hence why this should never be
        higher than this value. Defaults to `0.03`.

        - `cloud_scale`: Defines how much of the clouds can be seen on screen at the same
        time. This basically changes what could be considered the zoom of the shader. This 
        should always be a value higher than 1.0. If 1.0, the clouds are extremely zoomed in,
        but the larger the value is, the more zoomed out they are, and the more can be displayed
        on screen at the same time. Defaults to `2.0`.

        - `cloud_color`: The color of the clouds. This defaults to white (no shit), but can be changed
        for night time or for sunset/sunrise hues, among other use cases.

        - `sky_color_top`: The color of the top of the sky image, using three decimal numbers between
        0 and 1 defining the red, green and blue channels respectively. It should be noted that both top and
        bottom colors are mixed together to create a gradient, so using two slightly different values,
        like the default ones, can create a nice looking effect. Defaults to `(0.2, 0.4, 0.6)` (clear sky).

        - `sky_color_bottom`: The color of the bottom of the sky image. Defaults to `(0.4, 0.7, 1.0)`.

        - `cloud_cover`: This variable can be really tricky to use depending on the value used for 
        `cloud_scale`. In essence, this defines how much of the screen the clouds cover. A low value
        makes the clouds smaller, while a high value makes them larger. While I recommend to keep it 
        between -1 and 1, slightly lower/higher values can be used to match your needs. 
        For example, a high `cloud_scale` value with a high `cloud_cover` value will display a lot of
        very large clouds, while the other way around would only display a few small clouds.
        Should always be between -1 and 1. Defaults to `-0.3`.

        - `cloud_alpha`: This defines how opaque the clouds are. If 0.0, no clouds are displayed, which
        can be used for a customizable clear sky background. The higher the value is, the more opaque the
        clouds are, meaning you'll be less and less able to see the sky behind them. Using a value higher than 3
        is pointless, as you already won't be able to see through the clouds.

        - `wind_direction`: While I managed to add this parameter, using it required 3 specific values:
        `-2` for having the clouds moving to the right, `0` for only moving slightly (clouds can't stay in
        a single place) and `1`, the default, for moving to the left.

        As always, width and height can be changed to match the size you want (especially for using
        the effect for a sky mask behind a background). ATL can be used without a problem.
        """
        def __init__(self,
                        speed=0.03,                         #Should always be >= 0 and < 0.5
                        cloud_scale=2.0,                    #Should always be >= 1
                        cloud_color=(1.0, 1.0, 0.9),
                        sky_color_top=(0.2, 0.4, 0.6),
                        sky_color_bottom=(0.4, 0.7, 1.0),   
                        cloud_cover=-0.3,                   #Should always be between -1 and 1
                        cloud_alpha=2.0,                    #Should always be >= 0 and <= 3.
                        wind_direction=1.0,                 #Should always be -2, 0 or 1. 
                        width=1280,
                        height=720):

            super(Clouds, self).__init__()
            self.speed = float(speed)
            self.cloud_scale = float(cloud_scale)
            self.cloud_color = cloud_color
            self.sky_color_top = sky_color_top
            self.sky_color_bottom = sky_color_bottom
            self.cloud_cover = float(cloud_cover)
            self.cloud_alpha = float(cloud_alpha)
            self.wind_direction = float(wind_direction)
            self.width = width
            self.height = height
            self.child = Solid("#000", xysize=(self.width, self.height))
            self.start_time = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            r1 = renpy.render(self.child, self.width, self.height, st, at)
            rv = renpy.Render(self.width, self.height)
            rv.blit(r1, (0, 0))
            rv.mesh = True
            rv.add_shader("shaders.clouds")
            rv.add_uniform("u_time", elapsed)
            rv.add_uniform("u_speed", self.speed)
            rv.add_uniform("u_cloud_scale", self.cloud_scale)
            rv.add_uniform("u_cloud_color", self.cloud_color)
            rv.add_uniform("u_cloud_cover", self.cloud_cover)
            rv.add_uniform("u_cloud_alpha", self.cloud_alpha)
            rv.add_uniform("u_sky_color_bottom", self.sky_color_bottom)
            rv.add_uniform("u_sky_color_top", self.sky_color_top)
            rv.add_uniform("u_wind_direction", self.wind_direction)
            renpy.redraw(self, 0)
            return rv

#To only change specific parameters of the shader, specify the parameter name with its value:
# image clouds = Clouds(cloud_cover=0.5)    this only changes the cloud_cover default value.
image clouds = Clouds()
            