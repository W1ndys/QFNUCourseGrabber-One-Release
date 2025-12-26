import ddddocr
from flask import Flask, request, jsonify

app = Flask(__name__)
# 初始化OCR，禁用广告输出
ocr = ddddocr.DdddOcr(show_ad=False)


@app.route("/ocr", methods=["POST"])
def get_ocr_res():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # 读取图片内容
        image_bytes = file.read()

        # 识别
        res = ocr.classification(image_bytes)
        return jsonify({"result": str(res)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("启动 OCR 服务 (Flask)...")
    print("请确保已安装依赖: pip install ddddocr flask")
    # 监听本地 9898 端口
    app.run(host="127.0.0.1", port=9898)
