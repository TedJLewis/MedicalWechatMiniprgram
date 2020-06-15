//index.js
//获取应用实例
const app = getApp()


Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    avatarimg: {},
    username: "test",
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    xunlei: 'magnet:?xt=urn: btih: 1ED863FD652E61863F367AE2A58490237BABCEEE& dn=Mon.Inconnue.2019.1080p.WEB.x264 - worldmkv.mkv',
    imageList:{},
    text:"",
    openid:""
  },
  //事件处理函数
  inputText:function(e)
  {
    var that =this;
    that.setData({
      text:e.detail.value
    })

  },

  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    /*
    wx.navigateTo({
      url: '../userInfo/userInfo',
    }
    
    )
    */
    var that=this;
    
    wx.login({
      success(res){
            wx.getUserInfo({
              success: function (res) {
                console.log(res)
                that.setData({
                  userInfo: res.userInfo,
                  username: res.userInfo.nickName,
                  avatarimg: res.userInfo.avatarUrl,
                })

              }
            })
       
        if(res.code){
          var code=res.code;
          console.log('获取用户登录凭证： ' + code);
          wx.request({
            url:'http://127.0.0.1:8000/login/',
            method:'GET',
            data:{
              code:code,         
            },
            success(res){
              console.log(res)
       
              that.setData({
                openid: res.data[0].openid
              })
              app.globalData.openid = res.data[0].openid
            }
          })
        }else{
          console.log('login failed!'+res.errMsg)
        }
      }
    })
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },

  addImage:function(){
      var that=this
      wx.chooseImage({
        sizeType:"compressed",
        count:"9",
        success:function(res){
          console.log(res)
          console.log("openid:"+that.data.openid)
          that.setData({
            imageList:res.tempFilePaths
          })
   

        }
      })

     
  },

  upLoad: function() {
    var that = this
    for(var i=0; i<this.data.imageList.length; i++){
      var filePath = this.data.imageList[i]
      wx.uploadFile({
       // url: 'https://127.0.0.1:8000/image/',
        url: 'http://127.0.0.1:8000/image/',
        filePath: filePath,
        name: 'image',
        method: 'POST',
        formData: {
          'openid': that.data.openid,
          'text':that.data.text
        },
        success: function (res) {
          console.log(res);
         if(res.statusCode==200){
            wx.showToast({
              title: '上传成功！',
              duration: 3000
            });
          }
      
        }
      })
    }
   
   
    
    
  }
})
