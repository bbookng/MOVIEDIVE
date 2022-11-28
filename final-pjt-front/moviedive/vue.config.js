const { defineConfig } = require('@vue/cli-service')
const proxy = require('http-proxy-middleware')

module.exports = defineConfig({
  transpileDependencies: true,
})

module.exports = ({
  devServer: {
    proxy: 'https://moviedive.co.kr/'
  }
  // devServer: {
  //   proxy: {
  //     '/api': {
  //       target: 'https://moviedive.co.kr/api/',
  //       changeOrigin: true,
  //       pathRewrite: {
  //         '^/api': ''
  //       }

  //     }
  //   }
  // }
})