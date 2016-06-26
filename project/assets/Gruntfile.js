module.exports = function (grunt) {
    grunt.initConfig({
        sass: {
            dev: {
                options: {
                    outputStyle: 'expanded'
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
                    'input/js/**'
                ],
                dest: 'output/js/app.js',
            },
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
            }
        },

        watch: {
            sass: {
                files: ['input/sass/*'],
                tasks: ['sass:dev', 'copy:css']
            },
            scripts: {
                files: ['input/js/*'],
                tasks: ['concat', 'copy:js'],
            }
        }
    });

    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.registerTask('default', 'watch');
    grunt.registerTask('fonts', ['copy:fonts_devel', 'copy:fonts_prod']);
};
