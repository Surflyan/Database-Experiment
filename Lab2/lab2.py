# -*- coding: utf-8 -*-
"""
Created on Fri May 11 22:41:48 2018

@author: Surflyan
"""

import pymysql
import sys

def ConnectDb():
    print("Connect to mysql...")
    # 打开数据库连接
    db = pymysql.connect("localhost","root","19970128.","SCT")
    print("Connected!")
    return db


def main(argv):
    db = ConnectDb()
    cursor = db.cursor()

    if(argv[1] != "student_query" or argv[2] != "-q" or argv[4] != "-p" ):

        print("Error!")
        return
    else:
        query_parameter = argv[5]
        if(argv[3] == "1"):
            sql = "select S from SC where C='" + query_parameter + "'"

        elif(argv[3] == "2"):
            sql = "select C,Score from SC where S='" + query_parameter + "'"
        elif(argv[3]=="3"):
           sql = "select Sname from SC,Student,Course where Cname='" + query_parameter + "' and Course.C=SC.C and SC.S=Student.S"
        elif(argv[3]=="4"):
            sql = "select Cname,Chours,Credit,Csemester from Student,SC,Course where Sname='" + query_parameter + "' and SC.S=Student.S and SC.C=Course.C"
        elif (argv[3] == "5"):
            sql = "select Sname,C,Score from Student,SC where Score>'" + query_parameter + "' and SC.S=Student.S"
        elif(argv[3] == "6"):
            sql = "select S,avg(Score) from SC group by S having avg(Score)<'" + query_parameter + "'"
        elif(argv[3] == "7"):
            sql = "select count(C) from SC,Student where Sname='" + query_parameter + "' and Student.S=SC.S"
        elif(argv[3] == "8"):
            sql = "select Max(Score),Min(Score),Avg(Score) from SC, Course where Cname='" + query_parameter + "' and Course.C= SC.C"
        else:
            print("Error!")

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except:
            print("Error: unable to fecth data")


if __name__=="__main__":
    main(sys.argv)

