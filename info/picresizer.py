import os
import sys
import time
import glob
import Image

class PicResizer:
    """

    """
    def __init__(self,picpath,bakpath):
        ''''''
        self.picpath=picpath
        self.bakpath=bakpath

        logfile=bakpath+"/log"+time.strftime("%Y%m%d%H%M")+".txt"
        self.log=open(logfile,"a")

    def pic_walker(self,path):
        target=[]
        for files in glob.glob(path+"/*.jpg"):
            filepath,filename=os.path.split(files)#todo:mark
            target.append(filename)
        return target

    def check_folder(self,subFolderName):
        foldername=self.bakpath+'/'+subFolderName
        print foldername

        if not os.path.isdir(foldername):
            os.mkdir(foldername)
        return foldername

    def pic_info(self,img):
        w,h=img.size
        if w>h:
            return w,h,0
        else:
            return w,h,1

    def comp_num(self,x,y):
        x=float(x)
        y=float(y)
        return float(x/y)

    def pic_resize(self,picname,p_w,p_h):
        img=Image.open(picname)
        w,h,isVertical=self.pic_info(img)
        print w,h,isVertical
        if isVertical:
            p_w,p_h=p_h,p_w

        if self.comp_num(p_h,p_w)==self.comp_num(h,w):
            target=img.resize(
                (int(p_w),int(p_h)),
                Image.ANTIALIAS
            )
            #ANTIALIAS:a high-quality downsampling filter
            #BILINER:liner interpolation in a 2*2 environment
            #BICUBIC:cubic spline interpolaiton in a 4*4 environmant

            return target
        if self.comp_num(p_h,p_w) >self.comp_num(h,w):
            p_w_n=p_h*self.comp_num(w,h)
            temp_img=img.resize(
                (int(p_w_n),int(p_h)),
                Image.ANTIALIAS)
            c=(p_w_n-p_w)/2
            box=(c,0,c+p_w,p_h)
            box=tuple(map(int,box))
            target=temp_img.crop(box)
            return target
        else:
            p_h_n=p_w*self.comp_num(h,w)
            temp_img=img.resize(
                (int(p_w),int(p_h_n)),
                Image.ANTIALIAS
            )
            c=(p_h_n-p_h)/2
            box=(0,c,p_w,c+p_h)
            box=tuple(map(int,box))
            target=temp_img.crop(box)
            return target

    def run_auto(self,*args):
        imglist=self.pic_walker(self.picpath)

        for img in imglist:
            imgfile=self.picpath+"/"+img
            try:
                for std in args:
                    w,h=std[0],std[1]
                    opfile=self.check_folder(str(w)+"x"+str(h))+"/"+img
                    tmpimg=self.pic_resize(imgfile,int(w),int(h))
                    tmpimg.save(opfile,'jpeg')
                self.log.write(str(img)+"\tOK\n")
            except Exception,e:
                print e
                self.log.write(str(img)+"\tErr\n")
            print '-->'+img

        print "done"


def main():
    picpath="/home/matrix56/Projects/cquenv/media/images/devices"
    backpath="/home/matrix56/Projects/cquenv/media/images/devices"
    resizer=PicResizer(picpath,backpath)
    resizer.run_auto((200,200))
if __name__=="__main__":
    sys.exit(main())































