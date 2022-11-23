const { defineConfig } = require('@vue/cli-service')
const proxy = require('http-proxy-middleware')

module.exports = defineConfig({
  transpileDependencies: true,
})

module.exports = ({
  devServer: {
    proxy: 'http://localhost:8000/'
  }
  // devServer: {
  //   proxy: {
  //     '/api': {
  //       target: 'http://localhost:8000/api/',
  //       changeOrigin: true,
  //       pathRewrite: {
  //         '^/api': ''
  //       }

  //     }
  //   }
  // }
})