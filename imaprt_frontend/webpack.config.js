const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: './src/index.js',

    output: {
        path: `${__dirname}/public`,
        filename: "index.js"
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            },
            {
                test: /\.(ts|tsx)$/,
                use: 'ts-loader',
            },
            {
                test: /\.css$/,
                loaders: ['style-loader', 'css-loader?modules'],
            }
        ],
    },
    resolve: {
        extensions: [
            '.ts', '.tsx', '.js', '.jsx', '.css'
        ],
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: 'src/index.html',
            filename: 'index.html'
        })
    ]
};