module.exports = function (grunt) {
    grunt.initConfig({
        sass: {
            dev: {
                options: {
                    outputStyle: 'compressed',
                    sourcemap: 'none',
                    debugInfo: false
                },
                files: {
                    'output/css/styles.css': 'input/sass/styles.sass'
                }
            }
        },

        concat: {
            options: {
                separator: ';',
            },
            dist: {
                src: [
                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/bootstrap-sass/assets/javascripts/bootstrap.js',
                    'bower_components/moment/moment.js',
                    'bower_components/fullcalendar/dist/fullcalendar.js',
                    'bower_components/fullcalendar/dist/gcal.js',
                    'bower_components/fullcalendar/dist/lang/fi.js',
                    'bower_components/lightbox2/src/js/lightbox.js',
                    'input/js/**'
                ],
                dest: 'output/js/app.js',
            },
        },

        uglify: {
            my_target: {
                files: {
                    'output/js/app.js': [
                        'bower_components/jquery/dist/jquery.js',
                        'bower_components/bootstrap-sass/assets/javascripts/bootstrap.js',
                        'bower_components/moment/moment.js',
                        'bower_components/fullcalendar/dist/fullcalendar.js',
                        'bower_components/fullcalendar/dist/gcal.js',
                        'bower_components/fullcalendar/dist/lang/fi.js',
                        'bower_components/lightbox2/src/js/lightbox.js',
                        'input/js/*.js'
                    ]
                }
            }
        },

        copy: {
            main: {
                cwd: 'output',
                expand: true,
                src: '**',
                dest: '../sato/static/',
            },
            css: {
                cwd: 'output',
                expand: true,
                src: 'css/**',
                dest: '../sato/static/',
            },
            js: {
                cwd: 'output',
                expand: true,
                src: 'js/**',
                dest: '../sato/static/',
            },
            fonts_devel: {
                cwd: 'bower_components/font-awesome/',
                expand: true,
                src: 'fonts/**',
                dest: 'output/'
            },
            fonts_prod: {
                cwd: 'bower_components/font-awesome/',
                expand: true,
                src: 'fonts/**',
                dest: '../sato/static/'
            },
            lightbox_devel: {
                cwd: 'bower_components/lightbox2/src/images',
                expand: true,
                src: '**',
                dest: 'output/img/lightbox'
            },
            lightbox_prod: {
                cwd: 'bower_components/lightbox2/src/images',
                expand: true,
                src: '**',
                dest: '../sato/static/img/lightbox/'
            }
        },

        watch: {
            sass: {
                files: ['input/sass/**'],
                tasks: ['sass:dev', 'copy:css']
            },
            scripts: {
                files: ['input/js/**'],
                tasks: ['uglify', 'copy:js'],
            }
        }
    });

    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.registerTask('default', 'watch');
    grunt.registerTask('fonts', ['copy:fonts_devel', 'copy:fonts_prod']);
    grunt.registerTask('lightbox', ['copy:lightbox_devel', 'copy:lightbox_prod']);
};
