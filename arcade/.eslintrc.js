module.exports = {
    root: true,
    parserOptions: {
        ecmaVersion: 2020,
        sourceType: 'module',
    },
    overrides: [
        {
            files: ['*.ts'],
            parserOptions: {
                tsconfigRootDir: __dirname,
                project: ['tsc/tsconfig.json'],
                createDefaultProgram: true,
            },
            extends: [
                'plugin:@angular-eslint/ng-cli-compat',
                'plugin:@angular-eslint/ng-cli-compat--formatting-add-on',
                'plugin:@angular-eslint/template/process-inline-templates',
            ],
            rules: {
                '@angular-eslint/component-selector': [
                    'error',
                    {
                        type: 'element',
                        prefix: 'app',
                        style: 'kebab-case',
                    },
                ],
                '@angular-eslint/directive-selector': [
                    'error',
                    {
                        type: 'attribute',
                        prefix: 'app',
                        style: 'camelCase',
                    },
                ],
            },
        },
        {
            files: ['*.html'],
            extends: ['plugin:@angular-eslint/template/recommended'],
        },
    ],
};
