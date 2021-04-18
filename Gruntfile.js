const execs = {
    bandit: 'bandit --ini .bandit -r  -x "./venv" .',
    black: 'black . --exclude "venv|node_modules"',
    cspell: 'npx cspell -c .cspell.json {*,.*,**/*}',
    csscomb: 'npx csscomb . -t -v',
    doctest: 'pytest --doctest-modules',
    eslint: 'npx eslint . --fix',
    isort: 'isort .',
    mypy: 'mypy . --exclude venv',
    prettier: 'npx prettier . --write',
    pytest: 'pytest',
    quickdocs: 'quickdocs .quickdocs.yml',
    remark: 'npx remark -r .remarkrc .',
    sphinx: 'sphinx-build docs build',
};

execs['pylint'] = [
    'find .',
    '-name "venv" -prune',
    '-o -name "node_modules" -prune',
    '-o -iname "*.py" -print | xargs',
    'pylint --rcfile .pylintrc  --fail-under=8 .',
].join(' ');

const comprehension = (obj, cb) =>
    Object.fromEntries(Object.entries(obj).map(cb));

const testArgs = '--watch false --browsers ChromeHeadless';
const buildArgs = '--extra-webpack-config conf/extra.webpack.js';
const serveArgs = '--proxy-config conf/dev.proxy.conf.json';

const angular = comprehension(
    {
        'ng-serve': 'ng serve '.concat(serveArgs),
        'ng-build': 'ng run arcade:build:prod '.concat(buildArgs),
        'ng-ssr': 'ng run arcade:server:prod',
        'ng-unit': 'ng test '.concat(testArgs),
        'ng-integration': 'ng run arcade:integration '.concat(testArgs),
        'ng-e2e': 'ng e2e',
    },
    ([k, v]) => [k, { cmd: v, cwd: 'arcade' }]
);

const django = comprehension(
    {
        runserver: './startup/dev.sh',
    },
    ([k, v]) => [
        k,
        {
            cmd: 'PATH="./venv/bin" && '.concat(v),
            cwd: 'arcade_server',
        },
    ]
);

const docker = {
    image: {
        cmd: (name, env) =>
            [
                `docker build ${images[name].ctx}`,
                `-f ${images[name].ctx}/Dockerfile`,
                `--build-arg BUILD_TARGET=${env}`,
                `-t joellefkowitz/${name}:${env}`,
            ].join(' '),
    },
    push: {
        cmd: (name, env) => `docker push joellefkowitz/${name}:${env}`,
    },
};

const images = {
    arcade: { ctx: 'arcade' },
    arcade_nginx: { ctx: 'entry' },
    arcade_server: { ctx: 'arcade_server' },
    arcade_server_db: { ctx: 'postgres' },
};

module.exports = function (grunt) {
    grunt.initConfig({
        exec: {
            ...execs,
            ...angular,
            ...django,
            ...docker,
        },
    });

    grunt.loadNpmTasks('grunt-exec');

    grunt.registerTask(
        'lint',
        'Lint the source code',
        ['cspell', 'remark', 'pylint', 'bandit', 'mypy', 'eslint'].map((i) => 'exec:'.concat(i))
    );

    grunt.registerTask(
        'format',
        'Format the source code',
        ['prettier', 'csscomb', 'black', 'isort'].map((i) => 'exec:'.concat(i))
    );

    grunt.registerTask('tests:unit', 'Run unit tests', 
        ['doctest', 'pytest', 'ng-unit'].map((i) => 'exec:'.concat(i))
    );

    grunt.registerTask(
        'tests:integration',
        'Run integration tests',
        'exec:ng-integration'
    );

    grunt.registerTask('tests:e2e', 'Run e2e tests', 'exec:ng-e2e');

    grunt.registerTask(
        'docs:generate',
        'Generate a Sphinx documentation configuration',
        'exec:quickdocs'
    );

    grunt.registerTask(
        'docs:build',
        'Build documentation from a Sphinx configuration',
        'exec:sphinx'
    );

    grunt.registerTask('serve', 'Serve the arcade locally', 'exec:ng-serve');

    grunt.registerTask(
        'runserver',
        'Run arcade_server locally',
        'exec:runserver'
    );

    grunt.registerTask(
        'build',
        'Build arcade for the browser with production settings',
        'exec:ng-build'
    );

    grunt.registerTask(
        'ssr',
        'Run arcade for ssr with production settings',
        'exec:ng-ssr'
    );

    grunt.registerTask(
        'precommit',
        'Run a sequence of precommit quality control tasks',
        ['lint', 'tests:unit', 'docs:generate']
    );

    grunt.registerTask('images', 'Build docker images', (env) =>
        grunt.task.run(
            Object.keys(images).map((name) =>
                ['exec', 'image', name, env].join(':')
            )
        )
    );

    grunt.registerTask('push', 'Push docker images', (env) =>
        grunt.task.run(
            Object.keys(images).map((name) =>
                ['exec', 'push', name, env].join(':')
            )
        )
    );
};
