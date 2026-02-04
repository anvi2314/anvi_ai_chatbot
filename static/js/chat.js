const form = document.getElementById('chat-form');
const input = document.getElementById('message-input');
const chat = document.getElementById('chat');

function appendBubble(text, who='bot'){
  const el = document.createElement('div');
  el.className = 'bubble ' + (who === 'user' ? 'user' : 'bot');
  el.innerText = text;
  chat.appendChild(el);
  chat.scrollTop = chat.scrollHeight;
  return el;
}

function typingElement(){
  const el = document.createElement('div');
  el.className = 'bubble bot';
  el.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
  chat.appendChild(el);
  chat.scrollTop = chat.scrollHeight;
  return el;
}

form.addEventListener('submit', async (e) =>{
  e.preventDefault();
  const txt = input.value.trim();
  if(!txt) return;
  appendBubble(txt, 'user');
  input.value='';

  const typer = typingElement();

  try{
    const res = await fetch('/chat', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message: txt})});
    const j = await res.json();
    typer.remove();
    if(res.ok && j.reply){
      appendBubble(j.reply, 'bot');
    }else{
      appendBubble(j.error || 'Error from server', 'bot');
    }
  }catch(err){
    typer.remove();
    appendBubble('Network error: ' + err.message, 'bot');
  }
});
