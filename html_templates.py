HTML_PERSON = '''
<!DOCTYPE html>
<html lang="ru">
<head>
   <meta charset="UTF-8">
   <title>Направление на исследование</title>
   <style>
            * {
          margin: 0;
          padding: 0;
          font-family: 'Times New Roman', Times, serif;
          font-size: 13pt;
      }

      table { page-break-inside: auto;}
      tr    { page-break-inside: avoid; page-break-after: auto}
      thead { display: table-header-group }
      tfoot { display: table-footer-group }

      .print-container {}

      .research-header {
          padding-top: 12mm;
          display: flex;
      }

      .init-division-info {
          width: 55%;
      }

      .emblem-img {
          text-align: center;
      }

      .emblem-img > img {
          width: 33.6mm;
          height: 19.3mm;
      }

      .text-title-bold > p {
          font-weight: bold;
          text-align: center;
      }

      .text-title-bold > p {
          font-size: 11pt;
      }

      .text-bold {
          font-weight: bold;
          text-align: center;
      }

      .text-bold > p {
          font-size: 10pt;
      }

      .text {
          text-align: center;
      }

      .text > p {
          font-size: 11pt;
      }


      .hand-form {}

      .hand-form > table {
          width: 100%;
          text-align: center;
          font-size: 11pt;
      }

      .line {
          border-bottom: 1px solid black;
      }

      .addressees {
          width: 45%;
          padding-left: 27mm;
      }

      .post-division {}

      .rank-name {}

      .research-plot {}

      .plot-title {
          text-align: center;
          padding-top: 5mm;
          padding-bottom: 5mm;
      }

      .plot {
          display: flex;
          width: 100%;
      }

      .plot-event {
          width: 100%;
      }
      
      .sending_information {
          width: 100%;
          text-align: justify;
          text-indent: 12.5mm;
          margin-bottom
      }

      .qr-container {
          margin-top: 17mm;
          height: 50mm;
          display: flex;
          align-self: center;
          justify-content: space-between;        
          page-break-after: always;
          page-break-inside: avoid; 
      }

      .qr-image {
          width: 50mm;
          height: 50mm;
      }

      .permission {}

      .permission > p {
          text-indent: 12.5mm;
      }

      .annexes {}

      .annexes > p {
          text-indent: 12.5mm;
      }

      .research-person {
          padding-top: 5mm;
      }

      .person-table {
          display: flex;
          page-break-inside: avoid;
      }

      .serial-number {
          align-self: center;
          width: 10mm;
          font-size: 13pt;
          text-align: center;
      }
      
      .person-info-container {
          width: 100%;
      }
      
      .person-info {
          display: table-cell;
          height: 40mm;
          vertical-align: middle;
          
      }

      .person-qr {
          align-self: center;
          width: 40mm;
          height: 40mm;
      }

      .research-permission {
          padding-top: 15mm;
          page-break-inside: avoid;
      }

      .signatures {
          display: flex;
          width: 100%;
      }

      .signatures-initiator {
          width: 50%;
          text-align: left;
      }

      .signatures-initials {
          display: flex;
          width: 50%;
          justify-content: flex-end;
          align-self: flex-end;
      }

      .initials {}

      @media print {
          @page {
              size: A4;
          }
      }
   </style>
</head>
<body>
   <div class="print-container">
      <div class="research-header">
         <div class="init-division-info">
            <div class="text-title-bold">
               <p>{{ name }}</p>
               <br>
               <p>{{ regional_department }}</p>
            </div>
            <div class="text-bold">
               <br>
               <p>{{ research.initiator.division.division_full_name }}</p>
               <p>({{ research.initiator.division.division_red_name }})</p>
            </div>
            <div class="text">
               <p>{{ department_address }}</p>
               <br>
            </div>
            <div class="hand-form">
               <table>
                  <tr>
                     <td class="line" style="width: 10%"></td>
                     <td class="line" style="width: 35%"></td>
                     <td style="width: 10%">№</td>
                     <td class="line" style="width: 45%"></td>
                  </tr>
                  <tr>
                     <td style="width: 15%">на №</td>
                     <td class="line" style="width: 30%"></td>
                     <td style="width: 10%">от</td>
                     <td class="line" style="width: 45%"></td>
                  </tr>
               </table>
            </div>
            <div class="text">
               <br>
               <p>О направлении на исследование</p>
            </div>
         </div>
         <div class="addressees">
            <div class="post-division">
               <p>{{ research.addressee.post[0].upper() + research.addressee.post[1::] }} {{ research.addressee.division.division_red_name }}</p>
            </div>
            <br>
            <div class="rank-name">
               <p>{{ research.addressee.rank }}</p>
               <p>{{ research.addressee.create_name_reduction() }}</p>
            </div>
         </div>
      </div>
      <div class="research-plot">
         <div class="plot-title">
            <p>Направление на исследование</p>
         </div>
         <div class="sending_information">
                {% if persons|length > 1 %}
                <p>В связи с нижеизложенными обстоятельствами направляю в Ваш адрес буккальный эпителий лиц подлежащих проверке по федеральной
базе данных геномной информации (ФБДГИ)</p>
                {% else %}
                <p>В связи с нижеизложенными обстоятельствами направляю в Ваш адрес буккальный эпителий лица подлежащего проверке по федеральной
базе данных геномной информации (ФБДГИ)</p>
                {% endif %}
         </div>
         <br>
         <div class="plot">
            <div class="plot-event">
            {% if research.event.case_type == 'other' %}
               <p>Основание проверки: {{ research.event.number_to_string() }} от {{ research.event.convert_formation_date() }}</p>
            {% else %}
               <p>Основание проверки: {{ research.event.number_to_string() }} от {{ research.event.convert_formation_date() }};</p>
               <p>Статья: {{ '' if not research.event.article else research.event.article }};</p>
               <p>Событие: {{ '' if not research.event.plot else research.event.plot }};</p>
               <p>Дата происшествия: {{ research.event.convert_incident_date() }};</p>
               <p>Адрес места происшествия: {{ '' if not research.event.address else research.event.address }};</p>
            {% endif %}
            </div>
         </div>

      </div>
      <div class="research-person">
      {% for person in persons %}
         <div class="person-table">
            <div class="serial-number">{{ loop.index }}</div>
            <div class="person-info-container">
                <div class="person-info">
                   <p>Фамилия: {{ person.surname }}</p>
                   <p>Имя: {{ person.name }}</p>
                   <p>Отчество: {{ person.patronymic }}</p>
                   <p>Дата рождения: {{ person.convert_date() }} г.р.</p>
                   {% if research.related_search %}
                   <p>Степень родства: {{person.related}}</p>
                   {% endif %}
                </div>
            </div>    
            <div class="person-qr">
               <img class="person-qr" src="{{ person.img_path }}" alt="">
            </div>
         </div>
      {% endfor %}
      </div>
      <div class="research-permission">
         <div class="permission">
            {% if persons|length > 1 %}
            <p>Прошу установить генотипы проверяемых лиц и проверить по {% if research.related_search %} массиву неопознанных трупов {% endif %} ФБДГИ.  </p>
            {% else %}
            <p>Прошу установить генотип проверяемого лица и проверить его по {% if research.related_search %} массиву неопознанных трупов {% endif %} ФБДГИ.</p>
            {% endif %}
            <p>Разрешаю повреждение и уничтожение представленных объектов в размерах, необходимых для проведения
               исследования.</p>
         </div>
         <div class="annexes">
            <p>Приложение: конверт с образцом буккального эпителия ({{ persons|length }} шт.)</p>
         </div>
         <br>
         <br>
         <div class="signatures">
            <div class="signatures-initiator">
               <p>{{ research.initiator.post[0].upper() + research.initiator.post[1::] }}</p>
               <p>{{ research.initiator.rank }}</p>
            </div>
            <div class="signatures-initials">
               <div class="initials">
                  <p>{{ research.initiator.create_name_reduction() }}</p>
               </div>
            </div>
         </div>
         <div class="qr-container">
            <img class="qr-image" src="{{ research.dir_path + '\\initiator.png' }}" alt=""> 
            <img class="qr-image" src="{{ research.dir_path + '\\executor.png' }}" alt="">
            <img class="qr-image" src="{{ research.dir_path + '\\event.png' }}" alt="">        
         </div>
      </div>
   </div>
</body>
</html>
'''