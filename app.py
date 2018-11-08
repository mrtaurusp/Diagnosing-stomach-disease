from flask import Flask, render_template, request
import diagnostics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnostic', methods=['GET', 'POST'])
def diagnostic():
    if request.method == 'POST':
        res = request.form.getlist('check')

        P_hep_mon_vi = 0
        P_loet_da_day = 0
        P_viem_da_day = 0
        P_xuat_huyet_da_day = 0
        P_thung_da_day = 0
        P_ung_thu_da_day = 0

        for i in res:
            if i in diagnostics.hep_mon_vi:
                P_hep_mon_vi += diagnostics.hep_mon_vi[i]

        for i in res:
            if i in diagnostics.loet_da_day:
                P_loet_da_day += diagnostics.loet_da_day[i]

        for i in res:
            if i in diagnostics.viem_da_day:
                P_viem_da_day += diagnostics.viem_da_day[i]

        for i in res:
            if i in diagnostics.xuat_huyet_da_day:
                P_xuat_huyet_da_day += diagnostics.xuat_huyet_da_day[i]
 
        for i in res:
            if i in diagnostics.thung_da_day:
                P_thung_da_day += diagnostics.thung_da_day[i]
        
        for i in res:
            if i in diagnostics.ung_thu_da_day:
                P_ung_thu_da_day += diagnostics.ung_thu_da_day[i]
                
        return render_template('result.html', P_hep_mon_vi=P_hep_mon_vi, P_loet_da_day=P_loet_da_day, P_thung_da_day=P_thung_da_day,
                               P_ung_thu_da_day=P_ung_thu_da_day, P_viem_da_day=P_viem_da_day, P_xuat_huyet_da_day=P_xuat_huyet_da_day)
    return render_template('diagnostic.html', data=diagnostics.diagnostic)

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
