def clearScreen():
    print("\033c", end="")


def printLogo():
    print(
        """
                                                        .'''''.                 
     O$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$m'            )@$$$$$$,                
    "@$$$$%obpwZ0QUm$$$$$@hZZqpbkaMB$$$$@j            n$$$$$$$$t                
    t$$q           Y$$$$$M<           M$W+           jB$8*$$$$$Z`               
   .p$%^          ,h$$$$$b            B$h'          x$$8[?$$$$$Mi               
   >#@u.          ?&$$$$$t           "$$x         .u@$@_  *$$$$$t               
   ]dZ;           n$$$$$B`           lbb,         n$$&_   z$$$$$a               
                  b$$$$$O                        Y$$$]    ]8$$$$$+              
                 ;$$$$$${                       c@$8<     :h$$$$$0              
                 X$$$$$*!                     .J$$&?       Y$$$$$#!             
                `&$$$$$O'                    'U$$@>        <$$$$$B(             
                [B$$$$$f                     U$$W+          k$$$$$Q.            
                X$$$$$$I                   '0$$@-           /$$$$$8^            
               ,d$$$$$p                    C@$8l            lM$$$$$x            
               >B$$$$$}                  'm$$W-             `0$$$$$8.           
               v$$$$$M`                 `0$$$$$$$$$$$$$$$$$$$$$$$$$$[              
               W$$$$$C.                 q$$%akkkkkkkkkkkkkkkkh@$$$$$C.               
              ?$$$$$B(                "q$$@]                  b$$$$$aI               
              C$$$$$#i                m$$B!                   ($$$$$$[               
             ;h$$$$$q               ^k$$&]                    .%$$$$$O               
             ]8$$$$$)              "q$$%~                      Z$$$$$$:           
             c$$$$$B.             .o$$&~                       t$$$$$$v            
             h$$$$$L             ;b$$@-                        +W$$$$$o"             
       .^:l>{$$$$$$r>l:`.     ';<k$$@1l".                    ^I-o$$$$$8f!".          
     h@$$$$$$$$$$$$$$$$$$8} !o$$$$$$$$$$@r                "d@$$$$$$$$$$$$$@(         
     
           .`````.  ''     ''     .`;,`.   .'    `.     `.  .`````.  
           UC_++~" <*#i   ,p-   +aL+l![CI  XL.  u@z    1o,  Z0++++`  
          ^W?      fUq1   +b'  jq`        ,8}  ^&Xd   .wv  >#l       
          xh'      p-jc.  Qn  ra^         /W   )8Ial  ~M^  tm        
         "bt      >b;im' ;M+ i*i         `Ot  'Qr Or  xL   p[        
         ]*uuuuI  wz ,p, cp. fO   'YppO  ih`  la` (d. k_  >#zuuui    
         Yu      >%> .Ut:h}  Q/     ^m/  cY.  xJ. "#!?d,  mX         
         a<      up   (p}a   m{     >a` '#[  .*}   m{bv  >%~         
        tZ`     ,d_   l%Oj   nQ     Uz. th`  )a"   /mB!  ud          
       .WaZZZ0  +d'    k#i   'zWLtxQW] `dj  .pn    i8Z  ,dkZZZv.     
    """ + "\n"
    )


def spliter(size):
    for i in range(1, size):
        print("=", end="")
    print("=")


def printUi(text, options_array, clear_screen=False):
    # find longest
    split_lenght = 0
    for i in [y + f"| {len(options_array)} " for y in options_array] + [text]:
        if len(i) > split_lenght:
            split_lenght = len(i)
    while True:
        if clear_screen:
            clearScreen()
        spliter(split_lenght)
        print(text)
        spliter(split_lenght)
        for option_index, option_text in enumerate(options_array):
            print(f"| {option_index+1}) {option_text}")
        spliter(split_lenght)
        option = input(f"Select option: ")
        spliter(split_lenght)
        try:
            option = int(option)
            if option <= len(options_array):
                return option - 1
            else:
                continue
        except ValueError:
            continue
