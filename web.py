#!/usr/bin/python
# import our RPi.GPIO module and reference it as gpio

import RPi.GPIO as gpio
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from flask import Flask, redirect, url_for
import time

app = Flask(__name__)
tree = LEDBoard(*range(2,28),pwm=True)
function1Bool = True


@app.route("/")
def status():
    # get the current input state from our feedback loop
    input_state = gpio.input(17)
    # Check out input state and map it to a human readable status
    if input_state :
        led_status = "On"
    else:
        led_status = "Off" 
    #return """<html><body><div style="text-align: center;"></br><h3>Turn LED ...</h3><a href="/function2">Blink</a>  |  <a href="/on">On</a>  |  <a href="/off">Off</a><br> <a href="/blink0">Blink0</a>  |  <a href="/on0">On0</a>  |  <a href="/off0">Off0</a><br> <a href="/blink1">Blink1</a>  |  <a href="/on1">On1</a>  |  <a href="/off1">Off1</a><br> <a href="/blink2">Blink2</a>  |  <a href="/on2">On2</a>  |  <a href="/off2">Off2</a><br>  <a href="/blink3">Blink3</a>  |  <a href="/on3">On3</a>  |  <a href="/off3">Off3</a><br> <a href="/blink4">Blink4</a>  |  <a href="/on4">On4</a>  |  <a href="/off4">Off4</a><br> <a href="/blink5">Blink5</a>  |  <a href="/on5">On5</a>  |  <a href="/off5">Off5</a><br> <a href="/blink6">Blink6</a>  |  <a href="/on6">On6</a>  |  <a href="/off6">Off6</a><br><a href="/blink7">Blink7</a>  |  <a href="/on7">On7</a>  |  <a href="/off7">Off7</a><br>  </div>""" % led_status
    return """<html><body><div style="text-align: center;"></br><h3>Turn LED ...</h3><a href="/function2">Sparking</a>  |  </h3><a href="/function10">Blinking</a>  |  <a href="/function3">OneByOne</a>  |  <a href="/function4">Blinking2</a>  |  <a href="/function5">FromUp2Down</a>  |  <a href="/function6">Function6</a>  |  <a href="/function7">FromDown2Up</a>  |  <a href="/function8">Flashing</a>  |  <a href="/function9">Blinking3</a>  |  <a href="/on">On</a>  |  <a href="/off">Off</a><br><a href="/blink0">Blink0</a>  |  <a href="/on0">On0</a>  |  <a href="/off0">Off0</a><br><a href="/blink1">Blink1</a>  |  <a href="/on1">On1</a>  |  <a href="/off1">Off1</a><br><a href="/blink2">Blink2</a>  |  <a href="/on2">On2</a>  |  <a href="/off2">Off2</a><br><a href="/blink3">Blink3</a>  |  <a href="/on3">On3</a>  |  <a href="/off3">Off3</a><br> <a href="/blink4">Blink4</a>  |  <a href="/on4">On4</a>  |  <a href="/off4">Off4</a><br><a href="/blink5">Blink5</a>  |  <a href="/on5">On5</a>  |  <a href="/off5">Off5</a><br><a href="/blink6">Blink6</a>  |  <a href="/on6">On6</a>  |  <a href="/off6">Off6</a><br><a href="/blink7">Blink7</a>  |  <a href="/on7">On7</a>  |  <a href="/off7">Off7</a><br></div></body></html>"""
@app.route("/on")
def led_on():
    # Turn pin 4 on (high)
#    gpio.output(04,True)
    tree.on()
    return redirect(url_for('status'))

@app.route("/off")
def led_off():
    # Turn pin 4 off (low)
    tree.off()
    for led in tree:
        led.source_delay = 0
        led.source = [0]
    return redirect(url_for('status'))

@app.route("/blink0")
def blink0():
    tree[0].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off0")
def off0():
    tree[0].off()
    return redirect(url_for('status'))

@app.route("/on0")
def on0():
    tree[0].on()
    return redirect(url_for('status'))


@app.route("/blink1")
def blink1():
    tree[17].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off1")
def off1():
    tree[17].off()
    return redirect(url_for('status'))

@app.route("/on1")
def on1():
    tree[17].on()
    return redirect(url_for('status'))

@app.route("/blink2")
def blink2():
    tree[25].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[23].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[14].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[9].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off2")
def off2():
    tree[25].off()
    tree[23].off()
    tree[14].off()
    tree[9].off()
    return redirect(url_for('status'))

@app.route("/on2")
def on2():
    tree[25].on()
    tree[23].on()
    tree[14].on()
    tree[9].on()
    return redirect(url_for('status'))

@app.route("/blink3")
def blink3():
    tree[24].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[3].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[15].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off3")
def off3():
    tree[24].off()
    tree[3].off()
    tree[15].off()
    return redirect(url_for('status'))

@app.route("/on3")
def on3():
    tree[24].on()
    tree[3].on()
    tree[15].on()
    return redirect(url_for('status'))



@app.route("/blink4")
def blink4():
    tree[6].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[2].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[7].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[11].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off4")
def off4():
    tree[6].off()
    tree[2].off()
    tree[7].off()
    tree[11].off()
    return redirect(url_for('status'))

@app.route("/on4")
def on4():
    tree[6].on()
    tree[2].on()
    tree[7].on()
    tree[11].on()
    return redirect(url_for('status'))

@app.route("/blink5")
def blink5():
    tree[16].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[20].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off5")
def off5():
    tree[20].off()
    tree[16].off()
    return redirect(url_for('status'))


@app.route("/on5")
def on5():
    tree[20].on()
    tree[16].on()
    return redirect(url_for('status'))



@app.route("/blink6")
def blink6():
    tree[13].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[4].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[22].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[18].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[10].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off6")
def off6():
    tree[13].off()
    tree[4].off()
    tree[22].off()
    tree[18].off()
    tree[10].off()
    return redirect(url_for('status'))

@app.route("/on6")
def on6():
    tree[13].on()
    tree[4].on()
    tree[22].on()
    tree[18].on()
    tree[10].on()
    return redirect(url_for('status'))


@app.route("/blink7")
def blink7():
    tree[5].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[12].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[8].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[21].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    tree[19].blink(on_time=0.1, off_time=0.1, fade_in_time=1, fade_out_time=1, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/off7")
def off7():
    tree[5].off()
    tree[12].off()
    tree[8].off()
    tree[19].off()
    tree[21].off()
    return redirect(url_for('status'))

@app.route("/on7")
def on7():
    tree[5].on()
    tree[12].on()
    tree[8].on()
    tree[19].on()
    tree[21].on()
    return redirect(url_for('status'))

@app.route("/function1")
def function1():
    while function1Bool:
        on0()
        time.sleep(0.05)
        on1()
        time.sleep(0.05)
        on2()
        time.sleep(0.05)
        on3()
        time.sleep(0.05)
        on4()
        time.sleep(0.05)
        on5()
        time.sleep(0.05)
        on6()
        time.sleep(0.05)
        on7()
        time.sleep(1)
	off0()
	time.sleep(0.05)
	off1()
        time.sleep(0.05)
	off2()
        time.sleep(0.05)
	off3()
	time.sleep(0.05)
	off4()
	time.sleep(0.05)
	off5()
	time.sleep(0.05)
	off6()
	time.sleep(0.05)
	off7()
	time.sleep(0.5)	
    return redirect(url_for('status'))

@app.route("/function2")
def function2():
    for led in tree:
        led.source_delay = 0.1
        led.source = random_values()
    return redirect(url_for('status'))

@app.route("/function3")
def function3():

    tree[0].blink(on_time=2.5, off_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=2.4, off_time=0.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=2.3, off_time=0.3, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[23].blink(on_time=2.2, off_time=0.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[14].blink(on_time=2.1, off_time=0.5, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[9].blink(on_time=2.0, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(on_time=1.9, off_time=0.7, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[3].blink(on_time=1.8, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[15].blink(on_time=1.7, off_time=0.9, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.1, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[2].blink(on_time=1.5, off_time=1.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[7].blink(on_time=1.4, off_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[11].blink(on_time=1.3, off_time=1.3, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=1.2, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[20].blink(on_time=1.1, off_time=1.5, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=1.0, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[4].blink(on_time=0.9, off_time=1.7, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[22].blink(on_time=0.8, off_time=1.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[18].blink(on_time=0.7, off_time=1.9, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[10].blink(on_time=0.6, off_time=2.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[5].blink(on_time=0.5, off_time=2.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[12].blink(on_time=0.4, off_time=2.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[8].blink(on_time=0.3, off_time=2.3, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[21].blink(on_time=0.2, off_time=2.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[19].blink(on_time=0.1, off_time=2.5, fade_in_time=0, fade_out_time=0, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/function4")
def function4():
    tree[0].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[17].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[25].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[23].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[14].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[9].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[24].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[3].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[15].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[6].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[2].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[7].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[11].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[16].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[20].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[13].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[4].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[22].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[18].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[10].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    time.sleep(0.2)
    tree[5].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[12].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[8].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[21].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    tree[19].blink(on_time=0.2, off_time=0.2, fade_in_time=0.1, fade_out_time=0.1, n=None, background=True)
    return redirect(url_for('status'))


@app.route("/function5")
def function5():
    tree[0].blink(on_time=1.6, off_time=0.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=1.4, off_time=0.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[23].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[14].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[9].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[3].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[15].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[2].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[7].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[11].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=0.6, off_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[20].blink(on_time=0.6, off_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[4].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[22].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[18].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[10].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[5].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[12].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[8].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[21].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[19].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/function6")
def function6():
    tree[5].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[12].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[8].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[21].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[19].blink(on_time=0.2, off_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[4].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[22].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[18].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[10].blink(on_time=0.4, off_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=0.6, off_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[20].blink(on_time=0.6, off_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[2].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[7].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[11].blink(on_time=0.8, off_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[3].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[15].blink(on_time=1.0, off_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[23].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[14].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[9].blink(on_time=1.2, off_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=1.4, off_time=0.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[0].blink(on_time=1.6, off_time=0.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    return redirect(url_for('status'))

@app.route("/function7")
def function7():
    tree[5].blink(off_time=0.2,on_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[12].blink(off_time=0.2,on_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[8].blink(off_time=0.2,on_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[21].blink(off_time=0.2,on_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[19].blink(off_time=0.2,on_time=1.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(off_time=0.4,on_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[4].blink(off_time=0.4,on_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[22].blink(off_time=0.4,on_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[18].blink(off_time=0.4,on_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[10].blink(off_time=0.4,on_time=1.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(off_time=0.6,on_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[20].blink(off_time=0.6,on_time=1.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(off_time=0.8,on_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[2].blink(off_time=0.8,on_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[7].blink(off_time=0.8,on_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[11].blink(off_time=0.8,on_time=1.0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(off_time=1.0,on_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[3].blink(off_time=1.0,on_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[15].blink(off_time=1.0,on_time=0.8, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(off_time=1.2,on_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[23].blink(off_time=1.2,on_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[14].blink(off_time=1.2,on_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[9].blink(off_time=1.2,on_time=0.6, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(off_time=1.4,on_time=0.4, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[0].blink(off_time=1.6,on_time=0.2, fade_in_time=0, fade_out_time=0, n=None, background=True)
    return redirect(url_for('status'))


@app.route("/function8")
def function8():

    tree[0].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[23].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[14].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[9].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)	
    time.sleep(0.1)
    tree[24].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[3].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[15].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[2].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[7].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[11].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[20].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[4].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[22].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[18].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[10].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[5].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[12].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[8].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[21].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[19].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    ###
    time.sleep(0.1)
    tree[5].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[12].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[8].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[21].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[19].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[4].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[22].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[18].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[10].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[20].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[2].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[7].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[11].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[3].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[15].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[23].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[14].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    tree[9].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[0].blink(on_time=0.1, fade_in_time=0, fade_out_time=0, n=None, background=True)
    return redirect(url_for('status'))

	
@app.route("/function9")
def function9():
    tree[0].blink(on_time=0.1, off_time=0.1, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[17].blink(on_time=0.1, off_time=0.2, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    time.sleep(0.1)
    tree[25].blink(on_time=0.1, off_time=0.3, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[23].blink(on_time=0.1, off_time=0.3, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[14].blink(on_time=0.1, off_time=0.3, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[9].blink(on_time=0.1, off_time=0.3, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    time.sleep(0.1)
    tree[24].blink(on_time=0.1, off_time=0.4, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[3].blink(on_time=0.1, off_time=0.4, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[15].blink(on_time=0.1, off_time=0.4, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[6].blink(on_time=0.1, off_time=0.5, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[2].blink(on_time=0.1, off_time=0.5, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[7].blink(on_time=0.1, off_time=0.5, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[11].blink(on_time=0.1, off_time=0.5, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[16].blink(on_time=0.1, off_time=0.6, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[20].blink(on_time=0.1, off_time=0.6, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    time.sleep(0.1)
    tree[13].blink(on_time=0.1, off_time=0.7, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[4].blink(on_time=0.1, off_time=0.7, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[22].blink(on_time=0.1, off_time=0.7, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[18].blink(on_time=0.1, off_time=0.7, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[10].blink(on_time=0.1, off_time=0.7, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    time.sleep(0.1)
    tree[5].blink(on_time=0.1, off_time=0.8, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[12].blink(on_time=0.1, off_time=0.8, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    tree[8].blink(on_time=0.1, off_time=0.8, fade_in_time=0.2, fade_out_time=0.2, n=None, background=True)
    tree[21].blink(on_time=0.1, off_time=0.8, fade_in_time=0.2, fade_out_time=0, n=None, background=True)
    tree[19].blink(on_time=0.1, off_time=0.8, fade_in_time=0, fade_out_time=0.2, n=None, background=True)
    return redirect(url_for('status'))

	
@app.route("/function10")
def function10():
    for led in tree:
        led.source_delay = 0.8
        led.source = random_values()
    return redirect(url_for('status'))
	
	
@app.route("/function0on")
def function0on():
    return redirect(url_for('status'))

@app.route("/function0off")
def function0off():
    function0Bool = False
    return redirect(url_for('status'))

if __name__ == "__main__":
    # specify the setmode method were going to use, Im using the BCM mode, as this seems to corrolate with the wikis pin layout.
#    gpio.setmode(gpio.BCM)
    # register GPIO 3 as an output pin
#    gpio.setup(03,gpio.OUT)
    # register GPIO 16 as an input pin
#    gpio.setup(16,gpio.IN)
    app.run(host="0.0.0.0")
