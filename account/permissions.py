from rest_framework import permissions

# 프로필 조회를 API마다 필요한 권한이 달라 권한이 미리 조합된 클래스 활용
# 프로필에 대해 전체를 건드리는 요청이 없고 각 객체에 대한 요청만 있으므로 `has_object_permission()` 메서드를 가져와서 작성하면 된다.
#`permissions.SAFE_METHOD`는 GET 등 데이터에 영향을 주지 않는 메서드를 뜻한다.
# 즉 GET은 바로 True로 반환시키고, PUT/PATCH는 User 비교 결과를 반환시킨다.
# 즉 토큰이 유효하더라도 토큰의 User와 프로필의 User가 같지 않으면 통과시키지 않는다.

class CustomReadOnly(permissions.BasePermission):
    """커스텀 권한
    GET: 누구나
    PUT/PATCH: 해당 User만
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user