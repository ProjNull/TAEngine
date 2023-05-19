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
               v$$$$$M`                 `0$$$$$$$$$$$$$$$$$$$$$$$$$$[                .`````.  ''     ''     .`;,`.   .'    `.     `.  .`````.       
               W$$$$$C.                 q$$%akkkkkkkkkkkkkkkkh@$$$$$C.               UC_++~" <*#i   ,p-   +aL+l![CI  XL.  u@z    1o,  Z0++++`         
              ?$$$$$B(                "q$$@]                  b$$$$$aI              ^W?      fUq1   +b'  jq`        ,8}  ^&Xd   .wv  >#l              
              C$$$$$#i                m$$B!                   ($$$$$$[              xh'      p-jc.  Qn  ra^         /W   )8Ial  ~M^  tm               
             ;h$$$$$q               ^k$$&]                    .%$$$$$O             "bt      >b;im' ;M+ i*i         `Ot  'Qr Or  xL   p[               
             ]8$$$$$)              "q$$%~                      Z$$$$$$:            ]*uuuuI  wz ,p, cp. fO   'YppO  ih`  la` (d. k_  >#zuuui        
             c$$$$$B.             .o$$&~                       t$$$$$$v            Yu      >%> .Ut:h}  Q/     ^m/  cY.  xJ. "#!?d,  mX              
             h$$$$$L             ;b$$@-                        +W$$$$$o"           a<      up   (p}a   m{     >a` '#[  .*}   m{bv  >%~                
       .^:l>{$$$$$$r>l:`.     ';<k$$@1l".                    ^I-o$$$$$8f!".       tZ`     ,d_   l%Oj   nQ     Uz. th`  )a"   /mB!  ud                 
     h@$$$$$$$$$$$$$$$$$$8} !o$$$$$$$$$$@r                "d@$$$$$$$$$$$$$@(     .WaZZZ0  +d'    k#i   'zWLtxQW] `dj  .pn    i8Z  ,dkZZZv.            
    """ + "\n"
    )


def spliter(size):
    for i in range(1, size):
        print("=", end="")
    print("=")


def printUi(text, options_array, clear_screen=False):
    while True:
        if clear_screen:
            clearScreen()
        spliter(10)
        print(text)
        spliter(10)
        for option_index, option_text in enumerate(options_array):
            print(f"| {option_index+1}) {option_text}")
        spliter(10)
        option = input(f"Select option: ")
        spliter(10)
        try:
            option = int(option)
            if option <= len(options_array):
                return option - 1
            else:
                continue
        except ValueError:
            continue
