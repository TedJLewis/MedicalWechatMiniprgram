var app=getApp()
// pages/userInfo/userInfo.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userName:"李靖坦",
    genderData:"男",
    age:"28",
    firstTime:"2019-11-03",
    mobile:"17621341245",
    text1:"修改信息",
    text2:"保存信息",
    boolean:true,
    disabled:false,
    hasLogin:true,
    text:false,
    inputValueGender:{},
    inputValueAge: {},
    inputValueMobile: {},
    inputValueFirst: {},
  },

  
 
  textChange: function (e) {
     var bol=this.data.boolean;
     this.setData({
       boolean:!bol,
       text:!this.data.text,
       disabled:!this.data.disabled,
     })
     if(this.data.text==false){
       var openid = app.globalData.openid
       var name = this.data.userInfo.nickName
       var avatar = this.data.userInfo.avatarUrl
       var gender = this.data.inputValueGender
       var age = this.data.inputValueAge
       var mobile = this.data.inputValueMobile
       var first = this.data.inputValueFirst
       var that =this
      
       wx.request({
         url: 'http://127.0.0.1:8000/setinfo/',
         method: 'GET',
         data: {
           openid: openid,
           gender: gender,
           age: age,
           mobile: mobile,
           first:first,
           name:name,
           avatar:avatar,

         },
         success: function (res) {
           console.log(res);
           if (res.statusCode == 200) {
             wx.showToast({
               title: '修改信息成功！',
               duration: 3000
             });
             that.setData({              
               genderData: gender,
               age: age,
               firstTime: first,
               mobile: mobile,
               
             })
           }

         }
       })
     }
     
      

  },

    bindKeyInput: function (e) {
    this.setData({
      inputValueGender: e.detail.value
    })
  },

  bindKeyInput2: function (e) {
    this.setData({
      inputValueAge: e.detail.value
    })
  },

  bindKeyInput3: function (e) {
    this.setData({
      inputValueMobile: e.detail.value
    })
  },

  bindKeyInput4: function (e) {
    this.setData({
      inputValueFirst: e.detail.value
    })
  },

  webTest:function(event){
    wx.request({
      url:'http://www.ted1997.com',
      success:function(res){
        console.log(res)
      }
      
    })
  },
  clearLogin:function(){
    this.setData({
      userInfo:{},
      hasLogin:false
    })
  },

  login: function () {
    var that = this

    if (app.globalData.hasLogin == false) {
      wx.login({
        success: _getUserInfo
      })
    } else {
      _getUserInfo()
    }

    function _getUserInfo() {
      wx.getUserInfo({
        success: function (res) {
          that.setData({
            hasLogin: true,
            userInfo: res.userInfo
          })

        }
      })
    }
  },
/*
  login:function(){
    var that=this
    wx.login({
      success:function(){
      wx.getUserInfo({
        success: function (res){
          that.setData({
            hasLogin:true,
            userInfo:res.userInfo
          })
        }
      })
      }
    })
  },
  */
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this

    if (app.globalData.hasLogin == false) {
      wx.login({
        success: _getUserInfo
      })
    } else {
      _getUserInfo()
    }

    function _getUserInfo() {
      wx.getUserInfo({
        success: function (res) {
          that.setData({
            hasLogin: true,
            userInfo: res.userInfo
          })

        }
      })
    }
    var openid = app.globalData.openid
    wx.request({
      url: 'http://127.0.0.1:8000/initinfopage/',
      method: 'GET',
      data: {
        openid:openid
      },
      success(res) {
        console.log(res)

        that.setData({
          
          genderData: res.data[0].user[0].gender,
          age: res.data[0].user[0].age,
          firstTime: res.data[0].user[0].first_date,
          mobile: res.data[0].user[0].mobile,
         
          inputValueGender: res.data[0].user[0].gender,
          inputValueAge: res.data[0].user[0].age,
          inputValueMobile: res.data[0].user[0].mobile,
          inputValueFirst: res.data[0].user[0].first_date,  
        })
      }
    })  
    /** 
    this.setData({
      hasLogin: app.globalData.hasLogin
    })

    if (app.globalData.hasLogin == true)
      wx.getUserInfo({
        success: function (res) {
          that.setData({
            userInfo: res.userInfo
          })
        }
      })*/
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  // 上传图片
  doUpload: function () {
    // 选择图片
    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: function (res) {

        wx.showLoading({
          title: '上传中',
          duration:10000,
        })

        const filePath = res.tempFilePaths[0]
      }
    })
  },

        // 上传图片
        /*
        const cloudPath = 'my-image' + filePath.match(/\.[^.]+?$/)[0]
        wx.cloud.uploadFile({
          cloudPath,
          filePath,
          success: res => {
            console.log('[上传文件] 成功：', res)

            app.globalData.fileID = res.fileID
            app.globalData.cloudPath = cloudPath
            app.globalData.imagePath = filePath

            wx.navigateTo({
              url: '../storageConsole/storageConsole'
            })
          },
          fail: e => {
            console.error('[上传文件] 失败：', e)
            wx.showToast({
              icon: 'none',
              title: '上传失败',
            })
          },
          complete: () => {
            wx.hideLoading()
          }
        })

      },
      fail: e => {
        console.error(e)
      }
      
    })
    */

})