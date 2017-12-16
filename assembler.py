
register_number=range(32)
register_binary= [None]*32
register_name=["$zero","$at","$v0","$v1","$a0","$a1","$a2","$a3",'$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4',"$s5",'$s6','$s7','$t8','$t9','$k0','$k1','$gp','$sp','$fp',"$ra"]

R_format=["add","or","and","sub","nor","slt","sll","srl","jr"] ##R format instuctions
R_format_function=[32,37,36,34,39,42,0,2,8] ##R format instuctions function

I_format=["addi","ori","andi","slti","lui","lw","lh","lb","sw","sb","sh","beq","bne"] ##I format instuctions
I_op_code=[8,13,12,10,15,35,33,32,43,40,41,4,5]

for i in range(32) :
              register_binary[i]="%05d" % int(bin(register_number[i])[2:])

for i in range(len(R_format_function)) :
              R_format_function[i]="%06d" % int(bin(R_format_function[i])[2:])
              #print(R_format_function[i]+R_format[i])
for i in range(len(I_op_code)) :
              I_op_code[i]="%06d" % int(bin(I_op_code[i])[2:])
              #print(R_format_function[i]+R_format[i])
instruction = "begin"
#to.let.the.while.loop.work
path = input("enter the text file path and the name of the file with .txt extension and change the \ into / \n")
text_file = open(path, 'w')
while instruction != "quit":

    instruction = input("enter instruction\n")
    if instruction.find(",") :
        instruction=instruction.replace(",","")
    instruction_Sliced = instruction.split(" ")
    length_of_ins = len(instruction_Sliced)


    if instruction_Sliced[0] in R_format :
        print("//r format")
        print("//"+instruction)
        op_code_R_format = "%06d" % int(bin(0)[2:])

        if instruction_Sliced[0]=="sll" :
              rd = register_binary[register_name.index(instruction_Sliced[1])]
              rs = "%05d" % int(bin(0)[2:])
              rt = register_binary[register_name.index(instruction_Sliced[2])]
              temp=(instruction_Sliced[3])
              temp=int(temp)
              shamt = "%05d" % int(bin(temp)[2:])
        else :
              rd = register_binary[register_name.index(instruction_Sliced[1])]
              rs = register_binary[register_name.index(instruction_Sliced[2])]
              rt = register_binary[register_name.index(instruction_Sliced[3])]
              shamt = "%05d" % int(bin(0)[2:])
        func=R_format_function[R_format.index(instruction_Sliced[0])]
        print(op_code_R_format+" "+rs +" "+rt +" "+ rd+" "+shamt+" "+func)
        text=op_code_R_format+rs+rt+rd+shamt+func+'// R_format:  '+instruction+"\n"
        print(text)
        text_file.write(text)
    elif instruction_Sliced[0] in I_format :
        print("//I format")
        print("//"+instruction)
        op_code_I_format = I_op_code[I_format.index(instruction_Sliced[0])]
        if instruction_Sliced[0]=="lw" or instruction_Sliced[0]=="sw" :
              rs = (instruction_Sliced[3])
              if rs.find("(")>0 or rs.find(")")>0 :
                     rs = rs.replace("(", "")
                     rs = rs.replace(")", "")
                     rs = register_binary[register_name.index(rs)]

              else :
                     rs=register_binary[register_name.index(rs)]

              rt=register_binary[register_name.index(instruction_Sliced[1])]
              immediate=int(instruction_Sliced[2])
              immediate="%016d" % int(bin(immediate)[2:])
        elif instruction_Sliced[0]=="lui":
              rs = "%05d" % int(bin(0)[2:])
              rt = register_binary[register_name.index(instruction_Sliced[1])]
              immediate = int(instruction_Sliced[2])
              immediate = "%016d" % int(bin(immediate)[2:])
        else:

            rs=register_binary[register_name.index(instruction_Sliced[2])]
            rt = register_binary[register_name.index(instruction_Sliced[1])]
            immediate=int(instruction_Sliced[3])
            immediate = "%016d" % int(bin(immediate)[2:])



        print(op_code_I_format+" "+rs+" "+rt+" "+immediate)
        text = op_code_I_format + rs + rt + immediate +  '// I_format:  ' + instruction+'\n'
        print(text)
        text_file.write(text)
    elif instruction_Sliced[0] != "quit":
        print("error")




print("end")
text_file.close()