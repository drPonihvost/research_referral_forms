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
          font-family: Times New Roman, 'Times New Roman', Times, serif;
          font-size: 13pt;
      }

      table { page-break-inside: auto;}
      tr    { page-break-inside: avoid; page-break-after: auto}
      thead { display: table-header-group }
      tfoot { display: table-footer-group }

      .print-container {}

      .research-header {
          display: flex;
          padding-top: 17mm;
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
          padding-top: 19.3mm;
          padding-left: 27mm;
      }

      .post-division {}

      .rank-name {}

      .research-plot {}

      .plot-title {
          text-align: center;
          padding-top: 12.5mm;
          padding-bottom: 12.5mm;
      }

      .plot {
          display: flex;
          /*padding-bottom: 12.5mm;*/
          width: 100%;
      }

      .plot-event {
          width: 100%;
      }

      .qr-container {
          align-self: center;
      }

      .plot-qr {
          width: 40mm;
          height: 40mm;
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
      }

      .person-info {
          width: 100%;
          align-self: center;
      }

      .serial-number {
          width: 10mm;
          font-size: 13pt;
          text-align: center;
      }

      .person-qr {
          align-self: center;
          width: 40mm;
          height: 40mm;
      }

      .person-info {}

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
            <div class="emblem-img">
               <img src="data:image/jpeg;base64,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" alt="#">
            </div>
            <div class="text-title-bold">
               <p>{{ name }}</p>
               <p>{{ regional_department }}</p>
            </div>
            <div class="text-bold">
               <br>
               <p>{{ full_name_of_department }}</p>
               <p>({{ reduce_name_of_department }})</p>
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
               <p>{{ addressees_post.capitalize() }} {{ addressees_division }}</p>
            </div>
            <br>
            <div class="rank-name">
               <p>{{ addressees_rank }}</p>
               <p>{{ addressees_name }}</p>
            </div>
         </div>
      </div>
      <div class="research-plot">
         <div class="plot-title">
            <p>Направление на исследование</p>
         </div>
         <div class="plot">
            <div class="plot-event">
               <p>В связи с проведением проверки по: {{ case }};</p>
               <p>Статья: {{ article }};</p>
               <p>Событие: {{ plot }};</p>
               <p>Дата происшествия: {{ event_date }};</p>
               <p>Адрес: {{ event_address }};</p>
            </div>
            <div class="qr-container">
               <img class="plot-qr" src="{{ plot_qr_image }}" alt="">
            </div>
         </div>
      </div>
      <div class="research-person">
      {% for person in persons %}
         <div class="person-table">
            <div class="serial-number">{{ person.number }}</div>
            <div class="person-info">
               <p>Фамилия: {{ person.surname }}</p>
               <p>Имя: {{ person.name }}</p>
               <p>Отчество: {{ person.patronymic }}</p>
               <p>Дата рождения: {{ person.convert_date() }}</p>
               <p>Место рождения: {{ person.birthplace }} </p>
            </div>
            <div class="person-qr">
               <img class="person-qr" src="{{ person.img_path }}" alt="">
            </div>
         </div>
      {% endfor %}
      </div>
      <div class="research-permission">
         <div class="permission">
            <p>Прошу установить генотип проверяемого лица и проверить его по федеральной базе данных геномной информации
               (ФБДГИ).</p>
            <p>Разрешаю повреждение и уничтожение представленных объектов в размерах, необходимых для проведения
               исследования.</p>
         </div>
         <div class="annexes">
            <p>Приложение: конверт с образцом буккального эпителия ({{ person_count }} шт.)</p>
         </div>
         <br>
         <br>
         <div class="signatures">
            <div class="signatures-initiator">
               <p>{{ init_post.capitalize() }}</p>
               <p>{{ init_rank }}</p>
            </div>
            <div class="signatures-initials">
               <div class="initials">
                  <p>{{ init_name }}</p>
               </div>
            </div>
         </div>
      </div>
   </div>
</body>
</html>
'''