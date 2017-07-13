{% extends "main.tpl" %}

{% block title %}message{% end %}
{% block page_title %}Send message{% end %}
{% block subtitle %}Type something to panel</panel>{% end %}

{% block content %}
    <form class="pure-form pure-form-stacked" method="post">
        <fieldset>
            <legend>Message</legend>
            <input class="pure-input-2-3" name="msg" type="text" placeholder="message" required>
            <legend>Text color</legend>
            <label for="text_green" class="pure-checkbox">
                <input id="text_green" name="text_color" type="radio" value="text_green" checked>
                Green
            </label>
            <label for="text_red" class="pure-radio">
                <input id="text_red" name="text_color" type="radio" value="text_red">
                Red
            </label>
            <label for="text_orange" class="pure-radio">
                <input id="text_orange" name="text_color" type="radio" value="text_orange">
                Orange
            </label>
            <label for="text_black" class="pure-radio">
                <input id="text_black" name="text_color" type="radio" value="text_black">
                Black
            </label>

            <legend>Background color</legend>
            <label for="bg_black" class="pure-radio">
                <input id="bg_black" name="bg_color" type="radio" value="bg_black" checked>
                Black
            </label>
            <label for="bg_green" class="pure-radio">
                <input id="bg_green" name="bg_color" type="radio" value="bg_green">
                Green
            </label>
            <label for="bg_red" class="pure-radio">
                <input id="bg_red" name="bg_color" type="radio" value="bg_red">
                Red
            </label>
            <label for="bg_orange" class="pure-radio">
                <input id="bg_orange" name="bg_color" type="radio" value="bg_orange">
                Orange
            </label>
            <legend>Delay (sec)</legend>
                <label for="delay"></label>
                <select id="delay" name="delay">
                    <option>5</option>
                    <option>10</option>
                    <option>20</option>
                    <option>30</option>
                </select>
        </fieldset>
        <button type="submit" class="pure-button pure-button-primary">Send it!</button>
    </form>

{% end %}