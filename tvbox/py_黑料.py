{
  "replace" : {
    "http://127.0.0.1:10199" : "http://45.207.209.177:10199",
    "http://192.168.101.2:5050" : "http://ds.wya6.com:5000",
    "http://127.0.0.1:35455" : "http://ds.wya6.com:35455"
  },
  "sites" : [ {
    "key" : "php_music",
    "name" : "Music",
    "type" : 4,
    "api" : "https://demobe.serv00.net/music.php",
    "searchable" : 1,
    "style" : {
      "type" : "rect",
      "ratio" : 1
    }
  }, {
    "key" : "csp_NO视频",
    "name" : "❤️‍🔥〔NO视频丨XP™〕",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "数组" : "class=\"stui-vodlist__box&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "副标题" : "text-right\">&&</span>",
      "链接" : "href=\"&&\"",
      "搜索url" : "https://www.dgjiawu.com/se-1zxgt/{wd}-1",
      "起始页" : "2",
      "线路标题" : "NO视频",
      "播放数组" : "class=\"*-div&&</div>",
      "播放列表" : "class=\"btn btn-primary&&</a>",
      "播放标题" : ">&&</a>[不包含:蓝光]",
      "播放链接" : "href=\"&&\"",
      "分类url" : "https://www.dgjiawu.com/{cateId}/0/0/0/0/{catePg}[https://www.dgjiawu.com/{cateId}]",
      "分类" : "电影$mo-1zxgt/5738/1#电视剧$mo-1zxgt/5749/1#综艺$mo-1zxgt/5758/1#动漫$mo-1zxgt/5767/1"
    }
  }, {
    "key" : "NO视频",
    "name" : "NO视频",
    "type" : 3,
    "jar" : "https://2960.kstore.space/jar/XBPQ.jar",
    "api" : "csp_XBPQ",
    "playerType" : "2",
    "ext" : {
      "请求头" : "手机",
      "主页url" : "https://www.dgjiawu.com/",
      "简介" : "",
      "数组" : "class=\"stui-vodlist__thumb lazyload\"&&</a",
      "图片" : "data-original=\"&&\"",
      "链接" : "href=\"&&\"",
      "播放链接" : "href=\"&&\"",
      "标题" : "title=\"&&\"",
      "副标题" : "",
      "搜索url" : "",
      "嗅探词" : ".m3u8#https://m3u.hw8.live/share/#index.m3u8",
      "线路数组" : "href=\"javascript:;\"&&</li>",
      "线路标题" : "✨PYLB专享✨+class=\"v*\">&&</a[排序:线路2>>]",
      "播放数组" : "class=\"v*-div&&</div>",
      "播放列表" : "class=\"btn btn-primary btn-primary-ph&&</a",
      "播放标题" : ">&&</a",
      "倒序" : "0",
      "分类" : "电影$5738#电视剧$5749#动漫$5767#综艺$5758#你懂的$5748",
      "分类url" : "https://www.dgjiawu.com/mo-1zxgt/{cateId}/1/0/0/0/0/{catePg}[https://www.dgjiawu.com/mo-1zxgt/{cateId}/1];;RC"
    }
  }, {
    "key" : "天启",
    "name" : "❤️‍🔥〔天启丨XP™〕",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "数组" : "class=\"fed-list-item&&</li>",
      "标题" : "html\">&&</a>",
      "图片" : "data-original=\"&&\"",
      "副标题" : "center\">&&</span>",
      "链接" : "href=\"&&\"",
      "线路数组" : "<a href=\"#playlist*&&</li>",
      "线路标题" : "tab\">&&</a>",
      "分类url" : "https://www.sxmzie.com/by/{cateId}-{catePg}.html",
      "分类" : "电影&剧集&综艺&动漫",
      "分类值" : "1&2&3&4"
    }
  }, {
    "key" : "全看网",
    "name" : "❤️‍🔥〔全看网丨XP™〕",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "分类url" : "https://www.qkw1.cc/show/{cateId}--{by}------{catePg}---{year}.html",
      "分类" : "电影&剧集&综艺&动漫",
      "分类值" : "1&2&3&4"
    }
  }, {
    "key" : "黑木耳",
    "name" : "🍙木耳丨秒播",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "ext" : "DOCKER_ADDRESS/pg/lib/黑木耳资源.json",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar"
  }, {
    "key" : "热播库",
    "name" : "热播库",
    "type" : 3,
    "changeable" : 1,
    "api" : "csp_XBPQ",
    "playerType" : "1",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://rebozj.pro",
      "数组" : "class=\"stui-vodlist__thumb lazyload&&</a>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "副标题" : "class=\"pic-text text-right\"><b>&&</span>",
      "搜索模式" : "1",
      "嗅探词" : ".m3u8#video_mp4#tos-#.mp4#cdn.123pan.cn#huoshanvod.com",
      "搜索url" : "https://rebozj.pro/ajax/suggest?mid=1&wd={wd}&limit=500",
      "搜索二次截取" : "\"list\":[&&]",
      "搜索数组" : "{&&}",
      "搜索标题" : "\"name\":\"&&\"",
      "搜索图片" : "\"pic\":\"&&\"",
      "搜索链接" : "https://rebozj.pro/detail/+\"id\":&&,+html",
      "播放列表" : "<a&&/a>",
      "播放标题" : ">&&<",
      "影片类型" : "类型：&&</p>",
      "导演" : "导演：&&</p>",
      "主演" : "主演：&&</p>",
      "简介" : "display: none;\">&&</span>",
      "分类" : "电视剧$2#电影$1#综艺$3#动漫$4",
      "分类url" : "https://rebozj.pro/show/{cateId}--{area}------{catePg}---{year}.html;;a"
    }
  }, {
    "key" : "华为吧",
    "name" : "🏖️华为吧",
    "type" : 1,
    "api" : "http://127.0.0.1:10079/p/0/proxy/https://cjhwba.com/api.php/provide/vod/?ac=list",
    "playUrl" : "json:http://127.0.0.1:10079/parse/?thread=0&proxy=proxy&url=",
    "searchable" : 1,
    "quickSearch" : 1
  }, {
    "key" : "libhd",
    "name" : "libhd┃外剧",
    "type" : 3,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "api" : "csp_XBPQ",
    "ext" : {
      "主页url" : "https://www.libhd.com/",
      "分类" : "电影$1#电视剧$2#综艺$3#动漫$4",
      "搜索url" : "https://www.libhd.com/vodsearch/-------------.html?wd={wd}",
      "分类url" : "https://www.libhd.com/vodshow/{cateId}-{area}-{by}-{class}-{lang}----{catePg}---{year}.html;;akx",
      "图片" : "data-src=\"&&\"",
      "简介" : "text cor3&&</div>",
      "线路数组" : "swiper-slide&&</a>",
      "线路标题" : "</i>&&",
      "播放数组" : "anthology-list-box none&&</ul>"
    }
  }, {
    "key" : "csp_可可影",
    "name" : "可可影",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : "DOCKER_ADDRESS/pg/lib/可可影.json"
  }, {
    "key" : "PPT",
    "name" : "❤️‍🔥〔PPT丨XP™〕",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : "DOCKER_ADDRESS/pg/lib/ppt.json"
  }, {
    "key" : "亚色影库",
    "name" : "🔞亚瑟影库",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.yasetube.com/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "分类url" : "https://www.yasetube.com/video/category/{cateId}/page/{catePg}",
      "页面代理" : "proxy",
      "分类" : "女厕偷拍$nvce#海角系列$hj#FC2 PPV$fc2-ppv#Mesubuta系列$me#MILF人妻无码$milf#偷拍自拍$dalu#品牌传媒$madou"
    }
  }, {
    "key" : "php_madou",
    "name" : "麻豆",
    "type" : 4,
    "api" : "https://t4.doube.eu.org/madou.php",
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "style" : {
      "type" : "rect",
      "ratio" : 1.33
    }
  }, {
    "key" : "Netflav",
    "name" : "Netflav",
    "type" : 3,
    "api" : "csp_Netflav",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "timeout" : 60,
    "ext" : "https://netflav5.com$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    }
  }, {
    "key" : "奥斯卡",
    "name" : "🔞奥斯卡|采集",
    "type" : 1,
    "style" : {
      "type" : "rect",
      "ratio" : 1.6
    },
    "api" : "https://aosikazy.com/api.php/provide/vod",
    "playUrl" : "json:http://127.0.0.1:10079/parse/?thread=0&proxy=proxy&url="
  }, {
    "key" : "csp_XBPQ_JAV目錄大全",
    "name" : "🔞JAV｜大全",
    "type" : 3,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "ext" : {
      "热门推荐" : "1",
      "直接播放" : "0",
      "数组" : "<div class=\"card mx-1\">&&</a>[替换:alt=\"watermark\">>空]",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "搜索url" : "https://javmenu.cc/zh/search?wd={wd}&page={pg}",
      "搜索模式" : "1",
      "搜索数组" : "<div class=\"card mx-1\">&&</a>[替换:alt=\"watermark\">>空]",
      "搜索图片" : "data-src=\"&&\"",
      "搜索标题" : "alt=\"&&\"",
      "搜索链接" : "href=\"&&\"",
      "播放二次截取" : "id=\"pills-tabContent\">&&<div class=\"mb-3 col-12\">",
      "播放数组" : "<div class=\"single-video\">&&var server_count",
      "状态" : "更新：&&</span>",
      "导演" : "导演：&&</p>",
      "主演" : "主演：&&</p>",
      "简介" : "简介：&&</span>",
      "播放列表" : "<video id=\"&&</script>",
      "播放标题" : "couhe",
      "播放链接" : "m3u8.push(\"&&\"",
      "嗅探词" : ".m3u8",
      "播放请求头" : "",
      "分类" : "国产$chinese#五码$uncensored#欧美$western#fc2$fc2#女同性$115#三级字幕$442#91探花$455#偷拍自拍$278#国产传媒$390#台湾涩情$412",
      "分类url" : "https://javmenu.cc/zh/{cateId}/online?page={catePg}",
      "页面代理" : "proxy",
      "筛选" : "263"
    }
  }, {
    "key" : "追剧网",
    "name" : "💕追剧网",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "http://www.inpian.com/",
      "数组" : "class=\"myui-vodlist__box\"&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "简介" : "class=\"sketch hidden-sm hidden-xs\"&&</div>",
      "线路数组" : "class=\"item\"&&</div>",
      "线路标题" : ">云视频</a>",
      "分类url" : "http://www.inpian.com/search.php?page={catePg}&searchtype=5&order={by}&tid={cateId}&area=&year={year}&letter=&yuyan=&money=&ver=&jq=&state={letter}",
      "分类" : "国产剧$1#香港剧$2#韩国剧$3#欧美剧$4#台湾剧$5#日本剧$6#泰国剧$7"
    }
  }, {
    "key" : "色最色",
    "name" : "🔞色最色",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://xn--zovv42dba.com/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "分类url" : "https://xn--zovv42dba.com/list-read-id-{cateId}-p-{catePg}",
      "分类" : "国产精品$19#偷拍自拍$20#欧美成人$26#中文无码$23#中文字幕$22#亚洲情色$21#卡通动漫$24#成人伦理$25"
    }
  }, {
    "key" : "ppxdm",
    "name" : "💕ppx动漫",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.ppxdm.com/",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "图片" : "data-original=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "线路数组" : "class=\"module-tab-item tab-item\"&&</div>",
      "线路标题" : "<span>&&</span>",
      "分类url" : "https://www.ppxdm.com/v-show/{cateId}-{area}-{by}-{class}-{lang}-{letter}---{catePg}---{year}.html",
      "分类" : "动漫电影$1#日本动漫$2#国产动漫$3#欧美动漫$4#短剧$20"
    }
  }, {
    "key" : "222cuo",
    "name" : "🔞222cuo",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "http://224cuo.com/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "http://224cuo.com/{cateId}/list_{catePg}.html;;RC",
      "分类" : "亚洲AV$yazhouav#自拍偷拍$zipaitoupai#欧美AV$oumeiav#3D动画$3ddonghua#熟女人妻$shunvrenqi#丝袜制服$siwazhifu#主播直播$zhubozhibo#SM另类$smlinglei#亚洲性爱$yazhouxingai#偷拍自拍$toupaizipai#成人卡通$chengrenkatong#欧美性爱$oumeixingai#制服丝袜$zhifusiwa#经典三级$sanjijingdian#乱伦熟女$luanlunshunv#另类变态$lingleibiantai"
    }
  }, {
    "key" : "KanAV",
    "name" : "🔞KanAV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://kanav.info/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "数组" : "class=\"video-item\"&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://kanav.info/index.php/vod/type/id/{cateId}/page/{catePg}.html",
      "分类" : "中文字幕$1#日韩有码$2#日韩无码$3#国产AV$4#流出自拍$22#自拍泄密$30#探花约炮$31#主播录制$32#动漫番剧$20#里番$25#泡面番$26#Motion Anime$27#3D动画$28#同人作品$29"
    }
  }, {
    "key" : "AVTOP10",
    "name" : "AVTOP10",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "页面代理" : "proxy",
      "主页url" : "https://avtop10.com/",
      "头部集合" : "User-Agent$Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36#authority$avtop10.com#referer$https://avtop10.com/",
      "分类" : "最新影片&热门影片&高清影片&日本AV&欧美AV&动漫AV&中文字幕AV&无码AV&偷拍自拍&制服诱惑&人妻熟女&巨乳美乳&制服诱惑&学生校园&SM调教&网络红人&3P群交&乱伦家庭&强奸迷奸&性爱技巧&自慰诱惑",
      "分类值" : "1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20&21",
      "分类url" : "https://avtop10.com/api.php/provide/vod/?ac=list&ac=detail&t={cateId}&pg={catePg}",
      "数组二次截取" : "list\":[&&]",
      "数组" : "{&&}",
      "图片" : "vod_pic\"*\"&&\"",
      "标题" : "vod_name\"*\"&&\"",
      "副标题" : "vod_remarks\"*\"&&\"",
      "链接" : "https://avtop10.com/api.php/provide/vod/?ac=list&ac=detail&ids=+vod_id\":&&,",
      "搜索url" : "https://avtop10.com/api.php/provide/vod/?ac=detail&wd={wd}",
      "搜索模式" : "1",
      "搜索二次截取" : "list\":[&&]",
      "搜索数组" : "{&&}",
      "搜索图片" : "vod_pic\"*\"&&\"",
      "搜索标题" : "vod_name\"*\"&&\"",
      "搜索副标题" : "vod_remarks\"*\"&&\"",
      "搜索链接" : "https://avtop10.com/api.php/provide/vod/?ac=list&ac=detail&ids=+vod_id\":&&,",
      "影片类型" : "vod_class\"*\"&&\"",
      "导演" : "vod_director\"*\"&&\"",
      "主演" : "vod_actor\"*\"&&\"",
      "简介" : "vod_content\"*\"&&\"",
      "线路二次截取" : "\"list\":[&&]",
      "线路数组" : "\"vod_play_from\":&&,",
      "线路标题" : "\"&&\"",
      "播放数组" : "vod_play_url\":&&,[替换:\">>链表题#$>>题链#\\#>>链表表题]",
      "播放二次截取" : "",
      "播放列表" : "表&&表",
      "播放标题" : "题&&题",
      "播放链接" : "链&&链+?sku=OWY3ZDA4ZjVjYzY3YmRhYjM5NTUwYzEyZWRjNjUyZWM1NjQ2ZGRjYTVhMGVkM2Nh&p=1&sign=9a69d1563936ead3677623722660c4d9",
      "播放请求头" : "User-Agent$Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36#Referer$https://avtop10.com/#Cookie$PHPSESSID=t9a0fl2ngh4t175j3995v2669d",
      "嗅探词" : ".m3u8#.mp4#video_mp4#feiyunNB.mp4#.mp4#cdn.123pan.cn#huoshanvod.com"
    }
  }, {
    "key" : "19麻豆",
    "name" : "🔞19麻豆",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "站名" : "19麻豆",
      "主页url" : "https://19q.cc/",
      "分类url" : "https://19q.cc/index.php/vod/type/id/{cateId}/page/{catePg}.html",
      "分类" : "麻豆视频&91制片厂&天美传媒&蜜桃传媒&皇家华人&星空传媒&精东影业&乐播传媒&成人头条&乌鸦传媒&兔子先生&杏吧原创&玩偶姐姐&mini传媒&大象传媒&开心鬼传媒&萝莉社&PsychoPorn&性世界&糖心Vlog&性视界",
      "分类值" : "1&2&3&4&5&6&7&8&9&10&20&21&22&23&24&25&29&26&27&28&30",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "数组" : "<li>&&</li>",
      "图片" : "src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "副标题" : "<strong>&&</strong>"
    }
  }, {
    "key" : "18j.tv",
    "name" : "🔞18j.tv",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://18j.tv/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://18j.tv/show/{cateId}/nid/1/page/{catePg}/sid/1/",
      "页面代理" : "proxy",
      "分类" : "国产$1#日韩$2#欧美$3#伦理$4#动漫$16"
    }
  }, {
    "key" : "爱豆传媒",
    "name" : "🔞爱豆传媒",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://rourou.co/",
      "直接播放" : "1",
      "嗅探词" : "index.m3u8#.mp4#m3u8#.m3u8#/tos/#.flv#video/tos",
      "数组" : "class=\"myui-vodlist__box\">&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://rourou.co/index.php/vod/type/id/{cateId}/page/{carePg}.html",
      "分类" : "麻豆视频$1#中文字幕$2#日本无码$3#日本有码$4#童颜巨乳$5#校园萝莉$6#女优明星$7#角色扮演$8#制服诱惑$9#强奸乱伦$31#AI换脸$32#黑料泄密$33#主播直播$34#国产精品$35#探花视频$36#女同性恋$37#SM调教$38#人妻熟女$40"
    }
  }, {
    "key" : "唐人街",
    "name" : "💕唐人街",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.tangrenjie.one/",
      "数组" : "class=\"vodlist_thumb lazyload\"&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "简介" : "class=\"content_desc context clearfix\"&&</span>",
      "线路数组" : "class=\"play_source_tab list_scroll clearfix\"&&</div>",
      "线路标题" : ">&nbsp;<b>&&</b>",
      "分类url" : "https://www.tangrenjie.one/index.php/vod/show/area/{area}/id/{cateId}/letter/{letter}/page/{catePg}/year/{year}.html",
      "页面代理" : "proxy",
      "分类" : "电影$1#电视剧$2#动漫$3#综艺$4"
    }
  }, {
    "key" : "策驰影院",
    "name" : "💕策驰影院",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.cecidy.cc/",
      "数组" : "class=\"myui-vodlist__thumb lazyload\"&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "链接" : "href=\"&&\"",
      "简介" : "class=\"video-des\"&&</div>",
      "线路标题" : "data-toggle=\"tab\">&&</a>",
      "页面代理" : "proxy",
      "分类url" : "https://www.cecidy.cc/vodshow/{cateId}-{area}-{by}-{class}-{lang}-{letter}---{catePg}---{year}/",
      "分类" : "电影$1#剧集$2#综艺$3#动漫$4#短剧$60#动作片$6#喜剧片$7#爱情片$8#科幻片$9#恐怖片$10#剧情片$11#战争片$12#奇幻片$21#悬疑片$22#犯罪片$23#惊悚片$24#纪录片$25#国产剧$13#港台剧$14"
    }
  }, {
    "key" : "JAVSB",
    "name" : "🔞JAVSB",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://jav.sb/",
      "直接播放" : "1",
      "数组" : "class=\"relative aspect-w-16 aspect-h-9 rounded overflow-hidden shadow-lg\"&&</div>",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://jav.sb/javtype/{cateId}-{catePg}.html",
      "页面代理" : "proxy",
      "分类" : "日本有碼$Censored#日本無碼$Uncensored#FC2-PPV$FC2-PPV#無碼破解$Mosaic_Removed#中文字幕$CHN_SUB#MGS動画$MGS#寫真$Adult_IDOL#國產$Asian_Amateur"
    }
  }, {
    "key" : "18insta",
    "name" : "💗┃💋18INSTA┃💠",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    },
    "ext" : {
      "数组二次截取" : "models\":[&&]",
      "数组" : "{&&}",
      "图片" : "previewUrlThumbBig:\"https+://static-cdn.strpst.com/+https://static-cdn.strpst.com/&&\"",
      "标题" : "username\":\"&&\"",
      "副标题" : "id\":\"&&\"",
      "链接" : "hlsPlaylist\":\"&&_+_480p.m3u8",
      "分类url" : "https://zh.18insta.com/api/front/models?primaryTag=girls&sortBy=viewersRating&userRole=guest&groupId=6&limit=20&filterGroupTags=[[\"{cateId}\"]]&offset=0;;m",
      "直接播放" : 1,
      "播放请求头" : "手机",
      "分类" : "中国$tagLanguageChinese#乌克兰$tagLanguageUkrainian#日本$tagLanguageJapanese#韩国$tagLanguageKorean#越南$tagLanguageVietnamese#哥伦比亚$tagLanguageColombian"
    }
  }, {
    "key" : "pttred",
    "name" : "PTT | 影视",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : "DOCKER_ADDRESS/pg/lib/pttred.json"
  }, {
    "key" : "py_dm84",
    "name" : "DM84",
    "type" : 3,
    "api" : "https://gitee.com/dobebly/epg_-img/raw/master/py_dm84.py",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "changeable" : 1
  }, {
    "key" : "py_alist",
    "name" : " Alist网盘",
    "type" : 3,
    "api" : "https://9725.kstore.space/py_alist/py_alist.py",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "changeable" : 1,
    "ext" : {
      "json" : "DOCKER_ADDRESS/pg/lib/py_alist.json",
      "adult" : true,
      "missAvUrl" : "https://missav.live"
    }
  }, {
    "key" : "ppp",
    "name" : "🔞ppp",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.6
    },
    "ext" : {
      "主页url" : "https://ppp.porn/",
      "页面代理" : "proxy",
      "直接播放" : "1",
      "数组" : "<figure class=\"aspect-ratio\">&&</a",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "搜索url" : "https://ppp.porn/search/{wd}/",
      "搜索图片" : "data-src=\"&&\"",
      "搜索数组" : "<figure class=\"aspect-ratio\">&&</a",
      "分类url" : "https://ppp.porn/categories/{cateId}/{catePg}/;;a",
      "分类" : "中國AV$china-av#日本片商$japan-producer#素人自拍$amateur#中國$china#台灣$taiwan#日本$japan#東南亞$se-asia#韓國$korea#香港$hongkong#Cosplay$cosplay#主播$streamer#主觀視角$first-person-pov#凌辱$bdsm#劇情$drama#多P$threesome#探花$91-tanhua#流出$released#無碼$uncensored#百合$lesbian#野外露出$exhibitionists#OL$office-lady#動漫$ac#古裝$costume#女僕$maid#學生$student#旗袍$cheongsam#獸耳$kemonomimi#瑜伽褲$yoga-pants#真理褲$dolfin-shorts#空姐$flight-attendant#絲襪$pantyhose#護士$nurse#過膝襪$knee-socks"
    }
  }, {
    "key" : "NiceAv",
    "name" : "🔥NiceAv",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "直接播放" : "1",
      "页面代理" : "proxy",
      "图片" : "data-src=\"&&\"",
      "简介" : "⚠️慢点撸，皮要掉了！！！",
      "分类url" : "https://www.nice106.xyz/index.php/vod/type/id/{cateId}.html",
      "分类" : "中文字幕$1#日本有码$2#日本无码$3#AV解说$4#cosplay$5#黑丝诱惑$6#SWAG$7#自拍偷拍$8#激情动漫$9#网红主播$10#探花系列$11#三级伦理$12#VR视角$13#国产传媒$14#素人搭讪$15#门事件$16"
    }
  }, {
    "key" : "SOAV",
    "name" : "🔞SOAV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "主页url" : "https://777080.xyz/",
      "搜索url" : "https://777080.xyz/?s={wd}",
      "数组" : "data-video-uid=&&</div>",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "副标题" : "</i>&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "⚠️少看点，再看你就废了！！！",
      "分类url" : "https://777080.xyz/category/{cateId}/page/{catePg}/;;z",
      "分类" : "國產精選$國產精選#探花約炮$探花約炮#日韓影片$日韓影片#無碼素人$無碼素人#歐美專區$歐美專區#中字動漫$中字動漫"
    }
  }, {
    "key" : "AList",
    "name" : "六花@网盘|Alist[jar]",
    "type" : 3,
    "api" : "csp_AList",
    "searchable" : 1,
    "filterable" : 1,
    "changeable" : 1,
    "ext" : "DOCKER_ADDRESS/pg/js/alistjar_me.json",
    "jar" : "DOCKER_ADDRESS/pg/pg.jar"
  }, {
    "key" : "AnFuns",
    "name" : "💕AnFuns",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.anfuns.cc/",
      "数组" : "\"hl-list-item hl-col-xs-4 hl-col-sm-3 hl-col-md-20w hl-col-lg-2\"&&</li>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "副标题" : "hl-lc-1 remarks\">&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "简介：&&</li>",
      "分类url" : "https://www.anfuns.cc/type/{cateId}-{catePg}.html",
      "分类" : "新旧番剧$1#蓝光无修$2#动漫剧场$3#欧美动漫$4"
    }
  }, {
    "key" : "风车动漫",
    "name" : "💕风车动漫",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.dmla7.com/",
      "数组" : "stui-vodlist__box\"&&</div>",
      "图片" : "data-original=\"&&\"",
      "标题" : "title=\"&&\"",
      "副标题" : "pic-text text-right\">&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "text text-overflow text-muted hidden-xs\">&&</p>",
      "分类url" : "https://www.dmla7.com/type/{cateId}-{catePg}.html",
      "页面代理" : "proxy",
      "分类" : "日本动漫$ribendongman#国产动漫$guochandongman#动漫电影$dongmandianying#欧美动漫$omeidongman"
    }
  }, {
    "key" : "AVHAHA",
    "name" : "🔞AVHAHA",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "首页" : "亞洲AV影片$亞洲av影片",
      "主页url" : "http://www.avhaha.com/",
      "数组" : "\"col-md-4\"&&\"col-md-4\"",
      "图片" : "src=\"&&\"",
      "标题" : "title=\"&&\"",
      "副标题" : "class=\"views\">&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "⚠️慢点撸，皮要掉了！！！",
      "分类url" : "http://www.avhaha.com/category/{cateId}/page/{catePg}/;;z",
      "页面代理" : "proxy",
      "分类" : "亞洲AV影片$category/亞洲av影片#歐美AV影片$category/歐美av影片#中文字幕AV$tag/中文字幕#日本無碼$tag/亞洲無碼"
    }
  }, {
    "key" : "浮力ASMR",
    "name" : "🔞浮力ASMR",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "首页 " : "浮力ASMR$/",
      "主页url" : "https://flasmr.lol/",
      "分类url" : "https://flasmr.lol/page/{catePg}/[https://flasmr.lol/];;z",
      "页面代理" : "proxy",
      "分类" : "浮力ASMR$/"
    }
  }, {
    "key" : "海纳TV",
    "name" : "💕海纳TV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://hainatv.net/",
      "分类url" : "https://hainatv.net/index.php/vod/show/area/{area}/by/{by}/id/{cateId}/lang/{lang}/letter/{letter}/page/{catePg}/year/{year}.html",
      "分类" : "电影$1#剧集$2#综艺$3#动漫$4#短剧$59#解说$64"
    }
  }, {
    "key" : "直播转点播1",
    "name" : "🐼┃电视┃直播1",
    "type" : 3,
    "searchable" : 0,
    "api" : "https://famou.deno.dev/ediart/at/main/lib/live2vod.js",
    "ext" : "https://famou.deno.dev/ediart/at/main/lib/feimaolive.json"
  }, {
    "key" : "php2_del_ads_hmezy",
    "name" : "🤪 黑木耳(无广告)(T4_PHP)",
    "type" : 4,
    "api" : "https://t4.doube.eu.org/del_ads_heimuer.php",
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "changeable" : 0
  }, {
    "key" : "php2_hmezy",
    "name" : "🤪 黑木耳(T4_PHP)",
    "type" : 4,
    "api" : "https://t4.doube.eu.org/heimuer.php",
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "changeable" : 0
  }, {
    "key" : "php_huaweiba",
    "name" : "🤪 华为吧(T4_PHP)",
    "type" : 4,
    "api" : "https://t4.doube.eu.org/huaweiba.php",
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "changeable" : 0
  }, {
    "key" : "xp_nuiyue",
    "name" : "🤪 纽约影视(T3_Java)",
    "type" : 3,
    "api" : "csp_XPathFilter",
    "searchable" : 1,
    "quickSearch" : 0,
    "changeable" : 0,
    "filterable" : 1,
    "ext" : "https://t4.doube.eu.org/site/xp_nuiyue.json"
  }, {
    "key" : "玩偶妹妹",
    "name" : "玩偶妹妹",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "ext" : {
      "主页url" : "https://urcccg.dbtav9.today/cn/home/web/",
      "直接播放" : 1,
      "分类url" : "https://urcccg.dbtav9.today/vodtype/{cateId}/{catePg}/;;a",
      "分类" : "国产精品$20#主播大秀$21#唯美视频$22#口交视频$23#日本有碼$24#日本無碼$25#动漫视频$26#欧美视频$27#日韩视频$28#欧美视频$29#动漫视频$30#伦理影片$31"
    }
  }, {
    "key" : "黑木耳",
    "name" : "黑木耳",
    "type" : 1,
    "api" : "https://json.heimuer.xyz/api.php/provide/vod",
    "jar" : "./spider.jar",
    "categories" : [ "国产动漫", "欧美动漫", "日本动漫", "港台动漫", "国产剧", "欧美剧", "港剧", "韩剧", "日剧", "新马剧", "台剧", "国产综艺", "港台综艺", "韩国综艺", "日本综艺", "欧美综艺", "新马泰综艺", "其他综艺", "剧情片", "动作片", "冒险片", "喜剧片", "奇幻片", "恐怖片", "悬疑片", "惊悚片", "灾难片", "爱情片", "犯罪片", "科幻片", "动画电影", "泰剧", "其他剧", "歌舞片", "战争片", "经典片", "网络电影", "其它片", "逆袭短剧", "重生短剧", "穿越短剧", "甜宠短剧", "其它短剧", "新马泰动漫", "韩国动漫", "其它动漫" ],
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "changeable" : 0
  }, {
    "key" : "csp_Doll",
    "name" : "Doll",
    "type" : 3,
    "api" : "csp_Doll",
    "jar" : "https://t4.doube.eu.org/spider.jar;md5;3f392906996ac13aaeb8c91956f95f7fl",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1
  }, {
    "key" : "csp_Eighteen",
    "name" : "Eighteen",
    "type" : 3,
    "api" : "csp_Eighteen",
    "jar" : "https://t4.doube.eu.org/spider.jar;md5;3f392906996ac13aaeb8c91956f95f7fl",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1
  }, {
    "key" : "csp_Miss",
    "name" : "Miss",
    "type" : 3,
    "api" : "csp_Miss",
    "jar" : "https://t4.doube.eu.org/spider.jar;md5;3f392906996ac13aaeb8c91956f95f7fl",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1
  }, {
    "key" : "py_liushoushaofu",
    "name" : "🤪 留守少妇(T4_Py)",
    "type" : 4,
    "api" : "https://py.doube.eu.org/api?site=liushoushaofu",
    "searchable" : 0,
    "quickSearch" : 0,
    "filterable" : 0,
    "style" : {
      "type" : "rect",
      "ratio" : 1.33
    }
  }, {
    "key" : "Jablexbpq",
    "name" : "💗┃💋JableTV┃💠",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "主页url" : "https://jable.tv/",
      "数组" : "class=\"col-6 col-sm-4 col-lg-3\">&&class=\"sub-title\">&&</div>",
      "图片" : "data-src=\"&&\"",
      "标题" : "class=\"title\">*>&&</a",
      "链接" : "href=\"&&\"",
      "分类二次截取" : "class=\"app-nav\">&&</nav>",
      "分类数组" : "<a&&</a[不包含:按#優先]",
      "分类标题" : ">&&</a",
      "分类ID" : "href=\"https://jable.tv/&&/\"",
      "页面代理" : "proxy",
      "分类url" : "https://jable.tv/{cateId}/{catePg}/;;z"
    }
  }, {
    "key" : "高清无水印",
    "name" : "高清无水印",
    "type" : 3,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "api" : "csp_XBPQ",
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    },
    "ext" : {
      "直接播放" : "1",
      "图片" : "img src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://v3.bi888.link/vodtype/{cateId}-{catePg}.html",
      "分类" : "精品推荐$20#国产精品$21#日韩精品$22#欧美精品$23#中文字幕$24#日韩无码$25#日韩有码$26#网红主播$27#卡通动漫$28#探花系列$29#SM重味$30#自拍偷拍$31#强奸乱伦$32#口交视频$33#自慰系列$34#教师学生$35#3P合辑$36#巨乳系列$37#颜射系列$38#制服诱惑$39#萝莉少女$40#人兽之恋$41#人妻熟女$42#女同性恋$43#稀缺资源$45#三级伦理$44#空姐模特$48#国产盗摄$49#人妖系列$50#虚拟VR$51"
    }
  }, {
    "key" : "Bi8TV",
    "name" : "Bi8TV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    },
    "ext" : {
      "主页url" : "https://v3.bi888.link/",
      "直接播放" : "1",
      "图片" : "img src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "页面代理" : "proxy",
      "分类url" : "https://v3.bi888.link/vodtype/{cateId}-{catePg}.html",
      "分类" : "精品推荐$20#国产精品$21#日韩精品$22#欧美精品$23#中文字幕$24#日韩无码$25#日韩有码$26#网红主播$27#卡通动漫$28#探花系列$29#SM重味$30#自拍偷拍$31#强奸乱伦$32#口交视频$33#自慰系列$34#教师学生$35#3P合辑$36#巨乳系列$37#颜射系列$38#制服诱惑$39#萝莉少女$40#人兽之恋$41#人妻熟女$42#女同性恋$43#稀缺资源$45#三级伦理$44#空姐模特$48#国产盗摄$49#人妖系列$50#虚拟VR$51"
    }
  }, {
    "key" : "SOAV",
    "name" : "🔞SOAV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "主页url" : "https://www.wantav.co/",
      "搜索url" : "https://777080.xyz/?s={wd}",
      "数组" : "data-video-uid=&&</div>",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "副标题" : "</i>&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "⚠️少看点，再看你就废了！！！",
      "分类url" : "https://777080.xyz/category/{cateId}/page/{catePg}/;;z",
      "页面代理" : "proxy",
      "分类" : "國產精選$國產精選#探花約炮$探花約炮#日韓影片$日韓影片#無碼素人$無碼素人#歐美專區$歐美專區#中字動漫$中字動漫"
    }
  }, {
    "key" : "18AV",
    "name" : "🔞18AV",
    "type" : 3,
    "api" : "csp_Eighteen",
    "searchable" : 1,
    "timeout" : 60,
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    },
    "ext" : {
      "页面代理" : "proxy"
    }
  }, {
    "key" : "py_aidouchuanmei",
    "name" : "🤪 爱豆传媒(T4_py)",
    "type" : 4,
    "api" : "https://py.doube.eu.org/api?site=aidouchuanmei",
    "searchable" : 1,
    "quickSearch" : 0,
    "filterable" : 0,
    "style" : {
      "type" : "rect",
      "ratio" : 1.33
    }
  }, {
    "key" : "Bi8TV",
    "name" : "Bi8TV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    },
    "ext" : {
      "主页url" : "https://v3.bi888.link/",
      "直接播放" : "1",
      "图片" : "img src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "链接" : "href=\"&&\"",
      "分类url" : "https://v3.bi888.link/vodtype/{cateId}-{catePg}.html",
      "分类" : "精品推荐$20#国产精品$21#日韩精品$22#欧美精品$23#中文字幕$24#日韩无码$25#日韩有码$26#网红主播$27#卡通动漫$28#探花系列$29#SM重味$30#自拍偷拍$31#强奸乱伦$32#口交视频$33#自慰系列$34#教师学生$35#3P合辑$36#巨乳系列$37#颜射系列$38#制服诱惑$39#萝莉少女$40#人兽之恋$41#人妻熟女$42#女同性恋$43#稀缺资源$45#三级伦理$44#空姐模特$48#国产盗摄$49#人妖系列$50#虚拟VR$51"
    }
  }, {
    "key" : "SOAV",
    "name" : "🔞SOAV",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : {
      "主页url" : "https://www.wantav.co/",
      "搜索url" : "https://777080.xyz/?s={wd}",
      "数组" : "data-video-uid=&&</div>",
      "图片" : "data-src=\"&&\"",
      "标题" : "alt=\"&&\"",
      "副标题" : "</i>&&</span>",
      "链接" : "href=\"&&\"",
      "简介" : "⚠️少看点，再看你就废了！！！",
      "分类url" : "https://777080.xyz/category/{cateId}/page/{catePg}/;;z",
      "分类" : "國產精選$國產精選#探花約炮$探花約炮#日韓影片$日韓影片#無碼素人$無碼素人#歐美專區$歐美專區#中字動漫$中字動漫"
    }
  }, {
    "key" : "MissAV1",
    "name" : "Miss┃磁力",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "数组" : "img x-cloak&&/a></div></div>[不包含:item.title]",
      "图片" : "class=\"lozad*data-src=\"&&\"",
      "标题" : "<a class=\"text-secondary*>&&<",
      "副标题" : "<span class=\"absolute*>&&</span",
      "简介" : "keywords\" content=\"&&\"",
      "链接" : "href=\"&&\"",
      "搜索url" : "https://missav.com/cn/search/{wd}?page={pg}",
      "分类url" : "https://missav.com/{cateId}?page={catePg};;z",
      "分类" : "中文字幕$dm265/cn/chinese-subtitle#最近更新$dm509/cn/new#新作上市$dm504/cn/release#无码流出$dm558/cn/uncensored-leak#VR$cn/genres/VR#今日热门$dm242/cn/today-hot#本週热门$dm167/cn/weekly-hot#本月热门$dm206/cn/monthly-hot#SIRO$dm23/cn/siro#LUXU$dm20/cn/luxu#GANA$dm17/cn/gana#PRESTIGE PREMIUM$dm14/cn/maan#S-CUTE$dm23/cn/scute#ARA$dm19/cn/ara#无码流出$dm558/cn/uncensored-leak#FC2$dm94/cn/fc2#HEYZO$dm621/cn/heyzo#东京热$dm29/cn/tokyohot#一本道$dm39925/cn/1pondo#Caribbeancom$dm75695/cn/caribbeancom#Caribbeancompr$dm1200/cn/caribbeancompr#10musume$dm39286/cn/10musume#pacopacomama$dm663/cn/pacopacomama#Gachinco$dm135/cn/gachinco#XXX-AV$dm25/cn/xxxav#人妻斩$dm24/cn/marriedslash#顽皮 4610$dm19/cn/naughty4610#顽皮 0930$dm22/cn/naughty0930#麻豆传媒$dm31/cn/madou#TWAV$dm17/cn/twav#Furuke$dm14/cn/furuke",
      "页面代理" : "proxy"
    }
  }, {
    "key" : "18AV2",
    "name" : "🔞18AV2",
    "type" : 3,
    "api" : "csp_Eighteen",
    "searchable" : 1,
    "timeout" : 60,
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    }
  }, {
    "key" : "SeHuaTangpg",
    "name" : "🔞|色花|挂梯",
    "type" : 3,
    "api" : "csp_SeHuaTang",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "timeout" : 60,
    "ext" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber$$$proxy=proxy$$$1",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    }
  }, {
    "key" : "115Shareme",
    "name" : "六花@115云盘分享",
    "type" : 3,
    "api" : "csp_P115Share",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "timeout" : 120,
    "ext" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber$$$DOCKER_ADDRESS/pg/lib/me115.txt$$$db$$$1",
    "style" : {
      "type" : "list",
      "ratio" : 1.1
    },
    "jar" : "DOCKER_ADDRESS/pg/pg.jar"
  }, {
    "key" : "SeHuaTang",
    "name" : "色花堂",
    "type" : 3,
    "api" : "csp_SeHuaTang",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "timeout" : 120,
    "ext" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber$$$null$$$proxy",
    "style" : {
      "type" : "list",
      "ratio" : 1.1
    }
  }, {
    "key" : "Xojav",
    "name" : "XOJav",
    "type" : 3,
    "api" : "csp_Xojav",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    }
  }, {
    "key" : "csp_Netflav",
    "name" : "Netflav",
    "type" : 3,
    "api" : "csp_Netflav",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "ext" : "null$$$proxy",
    "timeout" : 60
  }, {
    "key" : "18AV1",
    "name" : "18AV",
    "type" : 3,
    "api" : "csp_Eighteen",
    "searchable" : 1,
    "recordable" : 0,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.485
    }
  }, {
    "key" : "MissAV",
    "name" : "MissAV",
    "type" : 3,
    "api" : "csp_Miss",
    "searchable" : 1,
    "recordable" : 0,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.78
    }
  }, {
    "key" : "Hanime",
    "name" : "Hanime",
    "type" : 3,
    "api" : "csp_Hanime",
    "searchable" : 1,
    "recordable" : 0,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 0.68
    }
  }, {
    "key" : "Jable",
    "name" : "Jable",
    "type" : 3,
    "api" : "csp_Jable",
    "searchable" : 1,
    "recordable" : 0,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "Cable",
    "name" : "CableAV",
    "type" : 3,
    "api" : "csp_Cable",
    "searchable" : 1,
    "quickSearch" : 1,
    "changeable" : 1,
    "filterable" : 0,
    "ext" : "null$$$proxy",
    "timeout" : 60
  }, {
    "key" : "top888",
    "name" : "AVtop",
    "type" : 3,
    "api" : "csp_Top888",
    "searchable" : 1,
    "timeout" : 60,
    "ext" : "null$$$proxy",
    "style" : {
      "type" : "rect",
      "ratio" : 1.6
    }
  }, {
    "key" : "NOWAV系列一",
    "name" : "️NOWAV.TV|热门女优",
    "type" : 3,
    "api" : "csp_XBPQ",
    "playerType" : 0,
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://nowav.tv",
      "页面代理" : "proxy",
      "数组" : "<div class=td-module-thumb&&</a></h3></div>",
      "图片" : "data-bg=url(&&)",
      "标题" : "title=\"&&\"",
      "简介" : "property=\"og:title\" content=\"&&\"><meta ",
      "链接" : "href=&&.html+.html",
      "跳转播放链接" : "",
      "直接播放" : "1",
      "嗅探词" : ".mp4#.m3u8#.flv#https://gr2ohi.azstream.xyz",
      "嗅探过滤词" : ".html#=http#suffixbigendtime=#.js#",
      "分类url" : "https://nowav.tv/tag/{cateId}/page/{catePg}",
      "分类" : "波多野結衣&深田えいみ&田中ねね&美谷朱里&松本いちか&篠田ゆう&明里つむぎ&逢見リカ&木下ひまり&浜崎真緒&姫咲はな&さつき芽衣&宮崎あやね&宮崎あや&森沢かな&浅野奈都紀&椎名空&JULIA&あや&立花メアリー&橘瑪麗&橘友美&市川悠子&夏目ゆみ&りあ&メアリさん&メアリー&椎名そら&橘メアリー&素人",
      "分类值" : "波多野結衣&深田えいみ&田中ねね&美谷朱里&松本いちか&篠田ゆう&明里つむぎ&逢見リカ&木下ひまり&浜崎真緒&姫咲はな&さつき芽衣&宮崎あやね&宮崎あや&森沢かな&浅野奈都紀&椎名空&JULIA&あや&立花メアリー&橘瑪麗&橘友美&市川悠子&夏目ゆみ&りあ&メアリさん&メアリー&椎名そら&橘メアリー&素人"
    }
  }, {
    "key" : "csp_JavDb",
    "name" : "JavDb",
    "type" : 3,
    "api" : "csp_JavDb",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "changeable" : 0,
    "style" : {
      "type" : "rect",
      "ratio" : 1.5
    },
    "ext" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber$$$null$$$proxy"
  }, {
    "key" : "JavBus",
    "name" : "JavBus",
    "type" : 3,
    "api" : "csp_JavBus",
    "filterable" : 1,
    "changeable" : 0,
    "style" : {
      "ratio" : 1.7
    },
    "timeout" : 60,
    "ext" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber$$$null$$$proxy"
  }, {
    "key" : "Youtube1",
    "name" : "Youtube1",
    "type" : 3,
    "api" : "csp_Youtube",
    "searchable" : 1,
    "quickSearch" : 0,
    "changeable" : 0,
    "timeout" : 120,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/youtube.json",
      "type" : "直播#新闻#剧集#电影#综艺#纪录片#音乐#体育#动物#风光#放松#4K#HDR#movie#music#documentary#bbc documentary#national geographic documentary",
      "keywords" : "排行榜,HOT,TRENDS,热门话题,热门趋势,热门综艺,热门电影,热门电视剧,小姐姐",
      "codecs" : "",
      "页面代理" : "proxy",
      "danmu" : true
    },
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "TGYunPanSS",
    "name" : "TG群组|涩涩网盘",
    "type" : 3,
    "api" : "csp_TGYunPan",
    "timeout" : 120,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.a.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "tgsearch_media_url" : "http://127.0.0.1:10199",
      "channellist" : "IPX_AV,pikpakziyuan,javdb91,zyfx_0315,cilitu,kc0102,ppg1314,cctav,avpush,avgc5200,ribenseyuge1,SeseAnime,vn666hh,avab01,bbw8562,CCCTAV,CCTAV1,nice_jav_daily,CosMM18",
      "proxy" : "noproxy",
      "danmu" : true
    },
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "TGYunPanSP",
    "name" : "TG群组|涩涩视频",
    "type" : 3,
    "api" : "csp_TGYunPan",
    "timeout" : 120,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.a.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "tgsearch_media_url" : "http://127.0.0.1:10199",
      "channellist" : "AVNVP,Seeyellow,ljqqyy,avwmjav,TPJPCP,avwmjavchat,sdafe4,TGJAV,gtkankan1,fbi2me,tumblrAce,AVnew,javcc,ttxsp,holozon,AVWUMAYUANPIAN,madou_77,wanninai,QiangJAv,xpzhenshi,fuligege4,jpccav,zuisewang,CTHHZY_3,BL666668,MadouVideos,FC2PPV91,fongmi_adult,MDFL88,wuma_liuchu,gaozhong1",
      "proxy" : "noproxy",
      "danmu" : true
    },
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "TGYunPanCG",
    "name" : "TG群组|吃瓜黑料",
    "type" : 3,
    "api" : "csp_TGYunPan",
    "timeout" : 120,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.a.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "tgsearch_media_url" : "http://127.0.0.1:10199",
      "channellist" : "wwkxa,cgblgw,jingpina,tplrwq",
      "proxy" : "noproxy",
      "danmu" : true
    },
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "TGYunPanLocal",
    "name" : "TG|正经",
    "type" : 3,
    "api" : "csp_TGYunPanLocal",
    "timeout" : 60,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "channellist" : "oneonefivewpfx,hao115,guaguale115,Channel_Shares_115,dianyingshare,XiangxiuNB,yunpanpan,kuakeyun,zaihuayun,Quark_Movies,vip115hot,yunpanshare,shareAliyun,ikiviyyp,alyp_1,quanziyuanshe",
      "proxy" : "proxy",
      "danmu" : true
    }
  }, {
    "key" : "TGYunPan",
    "name" : "TG|群组",
    "type" : 3,
    "api" : "csp_TGYunPan",
    "timeout" : 60,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "channellist" : "alypzyhzq,Mbox115,shares_115,Quark_Share_Channel,Aliyundrive_Share_Channel,wanwansubchat",
      "proxy" : "proxy",
      "danmu" : true
    }
  }, {
    "key" : "TGYunPan18+",
    "name" : "🍅TG18+群组|网盘搜索",
    "type" : 3,
    "api" : "csp_TGYunPan",
    "timeout" : 120,
    "ext" : {
      "token" : "DOCKER_ADDRESS/pg/lib/tokenm?token=amber",
      "json" : "DOCKER_ADDRESS/pg/lib/tgsearch.a.json",
      "keywords" : "名称,片名,推荐",
      "tgsearch_url" : "http://127.0.0.1:10199",
      "tgsearch_media_url" : "http://127.0.0.1:10199",
      "channellist" : "avwmjavchat|1000,IPX_AVTV|1000,kc0102|1000,ppg1314|1000,vn666hh|1000,IPX_AV|1000,pikpakziyuan|1000,avpush|1000,avgc5200|1000,cctav|1000,javdb91|1000,zyfx_0315|1000,ribenseyuge1|1000,vn666hh|1000,avab01|1000,CosMM18|1000,cilitu|1000,SeseAnime|1000",
      "proxy" : "noproxy",
      "danmu" : true
    },
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  }, {
    "key" : "JAVDAY",
    "name" : "🔞JAVDAY",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "数组" : "lazy loaded&&</a>",
      "页面代理" : "proxy",
      "图片" : "https://javday.tv+image: url(&&)",
      "链接" : "href=\"&&\"",
      "标题" : "class=\"title\"&&</span>",
      "副标题" : "播放+number\">&&</span>+次",
      "主演" : "list-item\"&&</a>",
      "分类url" : "https://javday.tv/category/{cateId}/page/{catePg}/;;z",
      "分类" : "無碼流出$uncensored-leaked#新作上市$new-release#有碼$censored#國產AV$chinese-av#糖心VLOG$txvlog#蘿莉社$luolisheus#HongKongDoll$hongkongdoll"
    }
  }, {
    "key" : "泥巴",
    "name" : "泥巴 | 海外",
    "type" : 3,
    "api" : "csp_NiNi",
    "searchable" : 1,
    "filterable" : 1,
    "changeable" : 0,
    "ext" : "0$$$127.0.0.1:10071|127.0.0.1:10073"
  }, {
    "key" : "csp_xBPQ_秒",
    "name" : "👩‍🎓秒播 | 文才推荐²",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 0,
    "ext" : "DOCKER_ADDRESS/pg/lib/文才.json",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar"
  }, {
    "key" : "XBPQ_毒蛇",
    "name" : "💞┃毒蛇┃💠",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "数组" : "class=\"module-item\">&&</div>",
      "图片" : "data-original=\"&&\"[替换:/vod1>>https://vres.a357899.cn/vod1]",
      "搜索url" : "https://dushe5.app/search?os=pc&k={wd}&page={pg}",
      "线路数组" : "<a&&</a>[排序:蓝光8>蓝光>FF线路]",
      "线路标题" : "class=\"source-item-label\">&&</span>",
      "分类url" : "https://dushe5.app/show/{cateId}-{class}-{area}-{lang}-{year}-{by}-{catePg}.html",
      "分类" : "电影&电视剧&动漫&综艺纪录&短剧",
      "分类值" : "1&2&3&4&6"
    }
  }, {
    "key" : " 茶杯狐",
    "name" : "  ‍🔥茶杯狐BPQ",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 0,
    "quickSearch" : 1,
    "filterable" : 1,
    "playerType" : "2",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "主页url" : "https://www.cupfox.cc",
      "数组" : "li class=\"fed-list-item fed-padding fed&&</li>",
      "图片" : "data-original=\"&&\"",
      "标题" : "fed-list-title*>&&</a>",
      "副标题" : "fed-text-center\">&&</span>",
      "线路数组" : "class=\"fed-padding fed-col-xs4&&</li>",
      "线路标题" : ">&&<",
      "跳转播放链接" : "var now=\"&&\"",
      "分类url" : "https://www.cupfox.cc/fox/{cateId}-{catePg}.html",
      "分类" : "电影&电视剧&综艺&动漫&伦理",
      "分类值" : "1&2&3&4&20"
    }
  }, {
    "key" : "PPTV06",
    "name" : " ‍🔥PPTV┃BPQ",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "ext" : {
      "分类url" : "https://www.pptv06.com/vodshow/{cateId}-{area}-------{catePg}---{year}.html",
      "分类" : "电影$1#电视剧$2#动漫$4"
    }
  }, {
    "key" : "wangfei",
    "name" : " ‍🔥网飞BPQ",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "https://qu.ax/ikKL.png",
    "ext" : {
      "线路数组" : "<div class=\"module-tab-item&&</div>[排序:][排序:HN线路>SO线路>KK线路]",
      "线路标题" : "<span>&&</small>[替换:</span><small>>>✮更新]",
      "分类url" : "https://www.wangfei.live/vodshow/area/{area}/by/{by}/id/{cateId}/page/{catePg}/year/{year}.html",
      "分类" : "电影$dy#剧集$juji#国产$guochanju#港剧$xianggangju#动漫$dongman"
    }
  }, {
    "key" : "XBPQ_AMD",
    "name" : " ‍🔥AMD|BPQ",
    "type" : 3,
    "api" : "csp_XBPQ",
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "搜索url" : "https://cms.fdue.de/index.php/vod/search.html?wd={wd}",
      "分类url" : "https://cms.fdue.de/index.php/vod/type/area/{area}/class/{class}/id/{cateId}/page/{catePg}/year/{year}.html",
      "分类" : "电影&连续剧&动漫",
      "分类值" : "1&2&4"
    }
  }, {
    "key" : "OK",
    "name" : " ‍🔥OK影视BPQ",
    "type" : 3,
    "api" : "csp_XBPQ",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "ext" : {
      "分类url" : "https://www.okys5.com/show/{cateId}-{area}-------{catePg}---{year}.html",
      "分类" : "电影$1#电视剧$2"
    }
  }, {
    "key" : "libhd",
    "name" : " ‍🔥利播BPQ",
    "type" : 3,
    "jar" : "DOCKER_ADDRESS/pg/lib/XBPQ.jar",
    "api" : "csp_XBPQ",
    "ext" : {
      "分类" : "电影$1#剧集$2#动漫$4",
      "搜索url" : "https://www.libhd.com/vodsearch/{wd}----------{pg}---.html",
      "分类url" : "https://www.libhd.com/vodshow/{cateId}-{area}--{class}-{lang}----{catePg}---{year}.html;;ak",
      "图片" : "data-src=\"&&\"",
      "简介" : "text cor3&&</div>",
      "线路数组" : "\"swiper-slide&&</a>[不包含:夸克]",
      "线路标题" : "</i>&&"
    }
  }, {
    "key" : "py_黑料18+",
    "name" : "黑料18+┃PY",
    "type" : 3,
    "api" : "DOCKER_ADDRESS/pg/lib/py_黑料.py",
    "searchable" : 1,
    "quickSearch" : 1,
    "filterable" : 1,
    "style" : {
      "type" : "rect",
      "ratio" : 1.77
    }
  } ]
}
