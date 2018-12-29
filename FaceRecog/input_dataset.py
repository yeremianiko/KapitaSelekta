import argparse
import cv2
import os
import sys

def main(args):
    datadir ='./train_img'
    cls_dir = os.path.join(datadir,args.cls)
    if not os.path.exists(cls_dir):
        os.makedirs(cls_dir)
    index_file = os.path.join(cls_dir,'index.txt')
    if not os.path.exists(index_file):
        last_index = 1
    else:
        with open(index_file,"r") as text_file:
            last_index = int(text_file.read())
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            while True:
                if cv2.waitKey(1) & 0xFF == ord('a'):
                    break
            filename = os.path.join(cls_dir,args.cls + '_' + str(last_index) + '.jpg')
            #print(filename)
            cv2.imwrite(filename,frame)
            last_index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            with open(os.path.join(cls_dir,'index.txt'),"w") as text_file:
                text_file.write(str(last_index))
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('cls', type=str, help='Member name')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
