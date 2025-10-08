function redirectToNewPage(eid, rid) {
    var inputEid = document.createElement('input');
    inputEid.type = 'hidden';
    inputEid.name = 'eid';
    inputEid.value = eid;

    var inputRid = document.createElement('input');
    inputRid.type = 'hidden';
    inputRid.name = 'rid';
    inputRid.value = rid;
    
    var csrfToken = document.createElement('input');
    csrfToken.type = 'hidden';
    csrfToken.name = 'csrfmiddlewaretoken';
    csrfToken.value = '{{ csrf_token }}';

    var form = document.createElement('form');
    form.method = 'POST';
    form.action = '/patient/problem/excercise/video/';
    form.appendChild(inputEid);
    form.appendChild(inputRid);
    form.appendChild(csrfToken);
    
    document.body.appendChild(form);
    form.submit();
}