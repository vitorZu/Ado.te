
let url_uf = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome'

$.getJSON(url_uf, function(data){
    let conteudo = '<option value="none" selected>----</option>';
    $.each(data, function(v,val){
       conteudo += '<option value="'+val.sigla+'">'+val.nome+'</option>';
    })

    $("#estado").html(conteudo)
})

let ufs = document.querySelector('#estado')

ufs.addEventListener('change', function(){
    var uf_selected = ufs.options[ufs.selectedIndex].value;
    console.log(uf_selected)
    let url_cidade = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'+uf_selected+'/municipios'
    
    $.getJSON(url_cidade, function(data){
        let conteudo;
        $.each(data, function(v,val){
           conteudo += '<option value="'+val.nome+'">'+val.nome+'</option>';
        })
    
        $("#cidade").html(conteudo)
    })
})

// Mask TEL

const handlePhone = (event) => {
    let input = event.target
    input.value = phoneMask(input.value)
  }
  
  const phoneMask = (value) => {
    if (!value) return ""
    value = value.replace(/\D/g,'')
    value = value.replace(/(\d{2})(\d)/,"($1) $2")
    value = value.replace(/(\d)(\d{4})$/,"$1-$2")
    return value
  }