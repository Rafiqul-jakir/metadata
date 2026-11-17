(function(){
var $=function(i){return document.getElementById(i)},I=JSON.parse($('i18n').textContent),P={s:'$99',p:'$199',e:'$299',c:null},cur=null;
$('yr').textContent=new Date().getFullYear();
var tb=$('rows'),fr=document.createDocumentFragment();(window.SAMPLE_DATA||[]).forEach(function(r){var tr=document.createElement('tr');r.forEach(function(c,i){var td=document.createElement('td');td.title=c;if(i==0||i==11){if(i==0){var a=document.createElement('a');a.href=c;a.target='_blank';a.rel='noopener nofollow';a.textContent=c;td.appendChild(a)}else td.textContent=c}else td.textContent=c;if(i==8)td.className='doi';tr.appendChild(td)});fr.appendChild(tr)});tb.appendChild(fr);
$('lang').addEventListener('change',function(e){try{localStorage.setItem('lang',e.target.selectedOptions[0].dataset.l)}catch(x){}location.href=e.target.value});
$('burger').onclick=function(){var m=$('menu'),o=m.classList.toggle('open');this.setAttribute('aria-expanded',o)};
document.querySelectorAll('#menu a').forEach(function(a){a.onclick=function(){$('menu').classList.remove('open')}});
document.querySelectorAll('[data-pkg]').forEach(function(b){b.onclick=function(){$('p').value=b.dataset.pkg;$('contact').scrollIntoView({behavior:'smooth'});$('n').focus({preventScroll:true})}});
function say(m,bad){$('ok').textContent=m;$('ok').style.color=bad?'#b91c1c':''}
function copy(t){if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(function(){say(I.ok)},function(){say(I.fail,1)})}else say(I.fail,1)}
$('cpmail').onclick=function(){copy(I.email)};
$('gen').onclick=function(){
 var n=$('n').value.trim(),e=$('e').value.trim(),o=$('o').value.trim(),k=$('p').value,m=$('m').value.trim(),er=$('err');er.textContent='';
 if(!n){er.textContent=I.errs[0];return}if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e)){er.textContent=I.errs[1];return}if(!k){er.textContent=I.errs[2];return}
 var i='spec'.indexOf(k);cur={s:I.subj[i],b:I.body.replace(/\{name\}/g,n).replace('{email}',e).replace('{org}',o||I.none).replace('{pkg}',I.opts[i]).replace('{price}',P[k]||I.custom).replace('{msg}',m||I.dm)};
 $('os').textContent=cur.s;$('ob').textContent=cur.b;$('out').hidden=false;say('');
 $('open').href='mailto:'+I.email+'?subject='+encodeURIComponent(cur.s)+'&body='+encodeURIComponent(cur.b);$('out').scrollIntoView({behavior:'smooth',block:'nearest'})};
$('c1').onclick=function(){copy(cur.s)};$('c2').onclick=function(){copy(cur.b)};$('c3').onclick=function(){copy(cur.s+'\n\n'+cur.b)};
})();
