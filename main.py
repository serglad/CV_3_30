import CV_2_25.documen_perspective_correction as pc
import Text_detection.text_detection as td
import shutil
import argparse
def PCDetect(fin,fout):
    '''
    Performs PC on fin then saves the result to "document.txt". Afterwards, performs text detection using EAST and saves the result to fout
    Args:
        fin(str): input image
        fout(str): output path
    '''
    try:
        pc.warp_perspective(fin,"document.png",None,None)
    except RuntimeError:
        shutil.copyfile(fin,"document.png")
        print("Document contours not found, searching the whole image")
    td.main("document.png",fout)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('fin')
    parser.add_argument('fout')
    args = parser.parse_args()
    
    PCDetect(args.fin, args.fout)