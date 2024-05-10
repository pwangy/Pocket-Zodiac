const path = require('path')

module.exports = {
	entry: './src/index.js', // the entry point of your application
	output: {
		path: path.resolve(__dirname, 'dist'), // where to output the bundled files
		filename: 'bundle.js' // the name of the bundled file
	},
	//   module: {
	//     rules: [
	// loaders for processing different types of files
	//     ]
	//   },
	resolve: {
		fallback: {
			path: require.resolve('path-browserify'),
			os: require.resolve('os-browserify/browser'),
			crypto: require.resolve('crypto-browserify')
		}
	}
}
