const { defineConfig } = require('@vue/cli-service')
const proxy = require('http-proxy-middleware')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
      // /accounts/profileimg/
      
    }

  }
})