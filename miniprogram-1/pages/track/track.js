// pages/upload/upload.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      reportData:["1"],
      a:'images/horizontal2.jpg',
      avatarimg:{},
      username:{},
      userInfo:{},
      id:{},

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
          wx.request({
            url: 'http://127.0.0.1:8000/downloadImage/',
            method: 'GET',
            data: {  
            },
            success(res) {
              console.log(res)
              that.setData({
                reportData: res.data[0].image
              })
            }
          })

   
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
        }
      })
      

 

          
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

  skipDetail(e) {
    let id = e.currentTarget.dataset.id
    // console.log("skip"+id)
    wx.navigateTo({ url: `/pages/reply/reply?id=${id}` });
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})