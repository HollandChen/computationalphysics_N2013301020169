line1 = {'c':'          ','h':'          ','e':'          ','n':'          ',\
         'y':'          ',' ':'          '}
line2 = {'c':'  #####   ','h':' #      # ','e':' ######## ','n':' #      # ',\
         'y':' #     #  ',' ':'          '}
line3 = {'c':' #        ','h':' #      # ','e':' #        ','n':' ##     # ',\
         'y':'  #   #   ',' ':'          '}
line4 = {'c':' #        ','h':' #      # ','e':' #        ','n':' # #    # ',\
         'y':'   # #    ',' ':'          '}
line5 = {'c':' #        ','h':' ######## ','e':' ######## ','n':' #  #   # ',\
         'y':'    #     ',' ':'          '}
line6 = {'c':' #        ','h':' #      # ','e':' #        ','n':' #   #  # ',\
         'y':'    #     ',' ':'          '}
line7 = {'c':' #        ','h':' #      # ','e':' #        ','n':' #    # # ',\
         'y':'    #     ',' ':'          '}
line8 = {'c':'  #####   ','h':' #      # ','e':' ######## ','n':' #     ## ',\
         'y':'    #     ',' ':'          '}
line9 = {'c':'          ','h':'          ','e':'          ','n':'          ',\
         'y':'          ',' ':'          '}
line = [line1,line2,line3,line4,line5,line6,line7,line8,line9]
name=raw_input('What do you want to type?')
ii,jj=1,1
while ii<=9 :
    line_print = ''
    while jj<=len(name) :
        line_print=line_print+line[ii-1][name[jj-1]]
        jj=jj+1
    print line_print
    jj=1
    ii=ii+1
