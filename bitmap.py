import sys


def main():
    map = """....................................................................

   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
                    
...................................................................."""
    text = list(sys.argv[1])
    lmap = map.splitlines(True)
    nmap = []

    for i in range(len(lmap)):
        for m in range(len(lmap[i])):
            if lmap[i][m].isspace():
                nmap.append(lmap[i][m])
            else:
                nmap.append(text[m % len(text)])
    print("".join(nmap))


if __name__ == "__main__":
    main()
