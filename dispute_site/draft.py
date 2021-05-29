{% load static %}
<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <title>disput</title>
        <link rel="stylesheet" href="{% static "css/header_footer.css" %}">
        <link rel="stylesheet" href="{% static "css/commentary.css" %}">
        <meta name="viewport" content="width=device-width">
    </head>

{% include 'header.html' %}

       <main class="main">
           <div style="margin-top:10px; display: flex; justify-content: space-between;">
               <p class="text">{{ question.user }}</p>
               <p class="text">{{ time }}</p>
           </div>
           <div id="header_main">
               <p id="block-name"> {{ question.header }} </p>
               <div id="for-quest" style="flex-grow: 1; display: flex;
                 flex-direction: row; align-self: center; align-items: center;
                   justify-content: flex-end">
                   <button id="btn_plus" class="btn" type="button" value="+" onclick="">+</button>
                   <button id="btn_minus" class="btn" type="button" value="-">-</button>
                   <input id="rate" name="rate_quest_input" type="number" value="{{ question.rating }}" class="counter">
               </div>
           </div>
           <div class="quest"> {{ question.text }} </div>
           <div style="margin-top:10px; display: flex; justify-content: flex-end;">
               <p class="text">Категория: {{ question.category }}</p>
           </div>
       </main>
       <main class="main">
           <div>
               <div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
                 <form method="POST" >
                 {% csrf_token %}
                   <div>
                       <div class="main-qwestion">{{commentform.as_p}}</div>
                   </div>
               </div>
               <!-- <input type="text" name="com_or_th" placeholder="1-теория, 0-комментарий"> -->
               <div style="margin: 5px 20px; flex-grow: 1; display: flex; flex-direction: row; align-self: center; align-items: center; justify-content: flex-end">
                    <input value="отправить" type="submit" class="send-btn" contenteditable="true">
               </div>
             </form>
           </div>
       </main>
       <div>
           <!-- здесь нужно будет сделать цикл по элементам  -->
           <div style="margin: 15px; margin-top:10px; display: flex; justify-content: space-between;">
               <button class="btn btn-comm-theory" type="button" id="theory" onclick="box_theory()">теории</button>
               <button class="btn btn-comm-theory" type="button"  id="comments" onclick="box_comm()">комментарии</button>
           </div>
           <div class="main" id="box-theory" style="display: none; flex-direction: column; align-self: center; align-items: center; justify-content: flex-end">
               <p class="text" style="align-self: flex-start;">user</p>
               <div class="theory">
                   <p class="comm"> Тут будет теория</p>
                   <div style="flex-grow: 1; display: flex;
                     flex-direction: row; align-self: center; align-items: center;
                       justify-content: flex-end">
                       <button id="bp1" class="btn btn-for-theory" type="button" onclick="plus()">+</button>
                       <button id="bm1" class="btn btn-for-theory" type="button" onclick="minus()">-</button>
                       <input type="number" readonly value="rate" class="counter">
                   </div>
               </div>
               <p class="text" style="align-self: flex-end;">time</p>
           </div>

           {% for comment in comments %}
               <div class="main" id="box-comm" style="display: none; flex-direction: column; align-self: center; align-items: center; justify-content: flex-end">
                   <p class="text" style="align-self: flex-start;">{{user}}</p>
                   <div class="quest for-comm"> {{text}} </div>
                   <p class="text" style="align-self: flex-end;">{{time}}</p>
               </div>
           {% endfor %}
       </div>

    <script>
        function box_theory() {
            let el = document.getElementById('box-theory');
            let el2 = document.getElementById('box-comm');
            if (el.style.display == 'none'){
                el.style.display = 'flex';
                el2.style.display = 'none'
            }
            else{
                el.style.display = 'none';
            }
        }

        function box_comm() {
            let el2 = document.getElementById('box-theory');
            let el = document.getElementById('box-comm');
            if (el.style.display == 'none'){
                el.style.display = 'flex';
                el2.style.display = 'none'
            }
            else{
                el.style.display = 'none';
            }
        }

        function box() {
            var parentDOM = document.getElementById("for-quest");
            var test=parentDOM.getElementsByClassName("btn");
            let els = document.getElementById('for-quest').getElementsByClassName('btn');
            var i;
            for (i = 0; i < els.length(); i++) {
                console.log(i)
            }
        }
    </script>
</html>
