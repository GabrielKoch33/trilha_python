'''
git init
-inicia um repo local .git na pasta do projeto/atual
-untracked (arquivos novos que não foram inseridos no git init)
-modified (arquivos que foram alterados depois que foram dados commit)
-added (arquivos em stage/preparação para commit)
-commit (mandar arquivos para o repo local e criar um savepoint)
'''

'''
git clone
-git clone https://github.com/owner/repo.git
-copia um repo remoto para sua máquina
'''

'''
git status
-git status // git status -s
-mostra arquivos modificados, não rastreados, staged
'''

'''
git add
-git add nome_arquivo //
-git add . (adiciona novos não rastreados e modificações, menos removidos) //
-git add -u (adiciona modificações e exclusões, menos arquivos novos não rastreados ) //
-git add -A (novos não rastreados, modificações e removidos) //
-adiciona/atualiza/exclui arquivos na área de preparação para o próximo commit
-mover mudanças para o staging antes do commit
'''
print('ACABEI DE DAR GIT ADD E COMMIT AQUI')
'''
git commit
-cria um commit com as mudanças staged, salvando um snapshot local com mensagem
-git commit -m "mensagem"
-git commit -a -m "Atualiza configurações" (faz git add + git commit)

-git commit --amend -m "altera mensagem"
    O Git pega o commit HEAD (o último commit), cria um novo commit. 
    O commit antigo deixa de ser referenciado por HEAD; o novo commit substitui HEAD.
-git add arquivo-esquecido.txt git commit --amend -m "Mensagem atualizada incluindo arquivo esquecido"
'''
print('OUTRO COMMIT SAVESTATE DESSE ARQUIVO COM COMMIT -A -M')
'''
git pull
-busca mudanças do remoto e as mescla na branch atual, atualizando sua branch local com mudanças remotas.
-git pull origin main
-git pull
'''

'''
git push
-envia commits locais para um repositório remoto/branch.
-git push origin main
-git push -u origin minha-feature (Enviar e definir upstream (para futuros push/pull automáticos)
'''

# Abrir projeto

# ↓
# git pull origin main

# ↓
# Programar

# ↓
# git add .

# ↓
# git commit -m "mensagem"

# ↓
# git push origin main