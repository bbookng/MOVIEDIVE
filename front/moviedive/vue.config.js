const { defineConfig } = require('@vue/cli-service')
// const proxy = require('http-proxy-middleware')

module.exports = defineConfig({
  transpileDependencies: true,
})

module.exports = ({
  // devServer: {
  //   proxy: {
  //     '/pimg': {
  //       target: 'http://127.0.0.1:800/api/accounts/profileimg/',
  //       changeOrigin: true,
  //       pathRewrite: {
  //         '^/api': ''
  //       }

  //     }
  //   }
  // }
})