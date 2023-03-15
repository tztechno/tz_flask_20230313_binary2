
import cv2
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import mpld3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    thres=128
    if request.method == 'POST':
        thres=int(request.form.get('thres', '128'))
        print('you selected',thres)
        img = cv2.imread('static/sample.png')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        threshold_val = thres
        max_val = 255
        threshold_type = cv2.THRESH_BINARY
        _, binary_img = cv2.threshold(gray_img, threshold_val, max_val, threshold_type)
        fig, axs = plt.subplots(1, 3, figsize=(5,2))
        axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[1].imshow(gray_img, cmap='gray')
        axs[2].imshow(binary_img)
        graph_html = mpld3.fig_to_html(fig)
        print('graph',thres)
        return render_template('index.html',graph_html=graph_html, thres=thres)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

