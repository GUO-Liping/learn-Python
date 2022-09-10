from PIL import Image as ImagePIL
import os

def transfer(infile, outfile):
	im = ImagePIL.open(infile)
	#im = im.resize((750,50))
	print(im.format, im.size, im.mode)
	im=im.convert('RGB')
	im.save(outfile, dpi=(300, 300)) #想要设定的dpi值

if __name__ == '__main__':
	for root, dirs, files in os.walk("chapter1_figs\\"): ##ori_ img为需要修改的图片存储的文件夹名字
		for item in files:
			list = item. split(".")
			print(list[-1])
			if(list[-1] == "png"):
				new_name = list[0] + ".png"
				os.rename("chapter1_figs\\" + item, "chapter1_figs\\" + new_name )
				print(new_name)
				transfer("chapter1_figs\\" + new_name, "chapter1_figs_dpi\\" + new_name )
