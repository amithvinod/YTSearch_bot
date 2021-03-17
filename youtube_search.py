from youtubesearchpython import VideosSearch

def get_video(param):
    
    
    
       videosSearch = VideosSearch(param)
       x = videosSearch.result()
       ids = []
       img = []
       title = []
       tim = []
       vc = []
       dur = []
       '''for i in result['result']: 
        print(i['id])
        print(i['link'])  #Video Link
        print(i['title']) #For Video Title'''
       av = x['result']
       for a in av:
          for p in a:
             if p == "id":
                ids.append(a[p])
             elif p =="title":
                title.append(a[p])
             elif p =="thumbnails":
                img.append(a[p][0]["url"])
             elif p =="publishedTime":
                tim.append(a[p])
             elif p =="viewCount":
                vc.append(a[p]['short'])
             elif p =="duration":
                dur.append(a[p])

       kk = {}
       kk['ids'] =ids
       kk['title'] =title
       kk['tim'] =tim
       kk['dur'] =dur
       kk['vc'] = vc
       kk['img'] =img
       
       return kk
           
       
   
              
              
       

    
       
    

'''def namevid(param):
    try:
       videosSearch = VideosSearch(param)
       x = videosSearch.result()
       av0 = x['result'][0]['title']
       av1 = x['result'][1]['title']
       av2 = x['result'][2]['title']
       av3 = x['result'][3]['title']
       av4 = x['result'][4]['title']
       av5 = x['result'][5]['title']
       av6 = x['result'][6]['title']
       av7 = x['result'][7]['title']
       av8 = x['result'][8]['title']
       av9 = x['result'][9]['title']
      
       
       
       

    except:
       av0,av1,av2,av3,av4= "error"
       
    return av0,av1,av2,av3,av4,av5,av6,av7,av8,av9

def imgvid(param):
    try:
       videosSearch = VideosSearch(param)
       x = videosSearch.result()
       
       
       av0 = x['result'][0]['thumbnails'][0]['url']
       av1 = x['result'][1]['thumbnails'][0]['url']
       av2 = x['result'][2]['thumbnails'][0]['url']

       av3 = x['result'][3]['thumbnails'][0]['url']
       av4 = x['result'][4]['thumbnails'][0]['url']
       av5 = x['result'][5]['thumbnails'][0]['url']
       av6 = x['result'][6]['thumbnails'][0]['url']
       av7 = x['result'][7]['thumbnails'][0]['url']
       av8 = x['result'][8]['thumbnails'][0]['url']
       av9 = x['result'][9]['thumbnails'][0]['url']
       
             
       
       

    except:
       av0,av1,av2,av3,av4= "error"
       
    return av0,av1,av2,av3,av4,av5,av6,av7,av8,av9
def ivid(para):
    
       videosSearch = VideosSearch(para)
       x = videosSearch.result()
       a = []
       
       av0 = x['result'][0]['duration']
       av1 = x['result'][1]['duration']
       av2 = x['result'][2]['duration']

       av3 = x['result'][3]['duration']
       av4 = x['result'][4]['duration']
       av5 = x['result'][5]['duration']
       av6 = x['result'][6]['duration']
       av7 = x['result'][7]['duration']
       av8 = x['result'][8]['duration']
       av9 = x['result'][9]['duration']

       bv0 = x['result'][0]['viewCount']['short']
       bv1 = x['result'][1]['viewCount']['short']
       bv2 = x['result'][2]['viewCount']['short']
       bv3 = x['result'][3]['viewCount']['short']
       bv4 = x['result'][4]['viewCount']['short']
       bv5 = x['result'][5]['viewCount']['short']
       bv6 = x['result'][6]['viewCount']['short']
       bv7 = x['result'][7]['viewCount']['short']
       bv8 = x['result'][8]['viewCount']['short']
       bv9 = x['result'][9]['viewCount']['short']

       cv0 = x['result'][0]['publishedTime']
       cv1 = x['result'][1]['publishedTime']
       cv2 = x['result'][2]['publishedTime']
       cv3 = x['result'][3]['publishedTime']
       cv4 = x['result'][4]['publishedTime']
       cv5 = x['result'][5]['publishedTime']
       cv6 = x['result'][6]['publishedTime']
       cv7 = x['result'][7]['publishedTime']
       cv8 = x['result'][8]['publishedTime']
       cv9 = x['result'][9]['publishedTime']
       if not (av0 is None):
           dv0 = list(av0+"  "+ bv0+ "  "+cv0)
           dv1 = list(av1+"  "+ bv1+ "  "+cv1)
           dv2 = list(av2+"  "+ bv2+ "  "+cv2)
           dv3 = list(av3+"  "+ bv3+ "  "+cv3)
           dv4 = list(av4+"  "+ bv4+ "  "+cv4)
           dv5 = list(av5+"  "+ bv5+ "  "+cv5)
           dv6 = list(av6+"  "+ bv6+ "  "+cv6)
           dv7 = list(av7+"  "+ bv7+ "  "+cv7)
           #dv8 = list(av8+"  "+ bv8+ "  "+cv8)
           dv9 = list(av9+"  "+ bv9+ "  "+cv9)
           hh = dv0+dv1+dv2+dv3+dv4+dv5+dv6+dv7+dv9
           a = a + hh
           print(a)

       
       else:
           pass
           print("josee")
           print(av0,av1,av2,av3,av4,av5,av6,av7,av8,av9)
             
       return a 
       

    
       
       

print(ivid("hi"))'''






    








