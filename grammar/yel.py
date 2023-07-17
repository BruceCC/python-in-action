# 喝点酒
def have_some_wine():
  print('先开一瓶酒，共有700毫升')
  wine = 700
  while wine > 0:
    # 取酒
    if wine > 200:
      get_wine = 200
      wine = wine - 200
    else:
      get_wine = wine
      wine = 0

    # 把酒送给客人
    print('您的酒来了：200毫升')
    yield get_wine
    print('函数执行完毕')



mywine = have_some_wine()
next(mywine)
next(mywine)

for i in mywine:
   print(f'我今天喝{i}毫升')


