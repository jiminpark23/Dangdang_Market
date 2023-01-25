from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Member

# Create your views here.

# 로그인 페이지
# 기능 1 : 로그인 화면 출력
# 기능 2 : 아이디, 비밀번호 입력받아서 로그인 되는 것

# 아이디, 비밀번호 입력받아 저장 후 홈으로 되돌아가기
def login(request):
    if request.method =='POST':
        user_id=request.POST.get('user_id')
        password=request.POST.get('password')

        # 확인하는 코드이기 때문에 조건문 안에 조건문을 써야 함
        if Member.objects.filter(user_id=user_id).exists():   # member 안의 user_id와 내가 가지고 온 user_id가 같은 데이터가 있는지 확인
            member = Member.objects.get(user_id=user_id)      # unique 옵션 때문에 id값이 1개일 수밖에 없음 -> get 함수 이용 가능
            
            if check_password(password, member.password):     # 입력받은 pw가 저장되어 있는 member.pw와 같으면
                # 로그인 성공!
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')
    
    # 로그인 실패!
        
    return render(request, 'login.html')    # 페이지 연결

def logout(request):
    # 세션에 존재하는지 확인 후 삭제
    if 'user_pk' in request.session:
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])
    
    return redirect('/')

# 회원가입 페이지 노출
# 회원가입 기능 개발
def register(request):
    if request.method =='POST':
        member = Member(
            user_id=request.POST.get("user_id"),
            password=make_password(request.POST.get("password")),   # 비밀번호 암호화 해서 저장
            name=request.POST.get("name"),
            age=request.POST.get("age"),           
        )
        member.save()
        return redirect('/member/login/')    
    return render(request, 'register.html')