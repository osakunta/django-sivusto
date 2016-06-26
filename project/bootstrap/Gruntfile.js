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
                src: ['node_modules/jquery/dist/jquery.js', 'assets/javascripts/bootstrap.js', 'input/js/*'],
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
    grunt.registerTask('default', 'watch')
};
