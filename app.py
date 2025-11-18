from flask import Flask  
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Proyek BNSP : Layanan Terintegrasi Berhasil di-Deploy!<h1><p>Ini adalah demo CI/CD Docker dan VPS.</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)