#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 5
//과제 추가한거임!!!!!!!!!!!!!!!!!!!!!!!!!!!!ㅃ
typedef struct songtype
{
    int num;
    int time;
} element;

typedef struct
{ // 큐 타입
    element data[MAX_QUEUE_SIZE];
    int front, rear;
} DequeType;

// 오류 함수
void error(const char *message)
{
    fprintf(stderr, "%s\n", message);
    exit(1);
}

// 초기화
void init_deque(DequeType *q)
{
    q->front = q->rear = 0;
}

// 공백 상태 검출 함수
int is_empty(DequeType *q)
{
    return (q->front == q->rear);
}

// 포화 상태 검출 함수
int is_full(DequeType *q)
{
    return ((q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}
// 원형큐 출력 함수
void deque_print(DequeType *q)
{
    if (!is_empty(q))
    {
        int i = q->front;
        do
        {
            i = (i + 1) % (MAX_QUEUE_SIZE);
            printf(" %d | ", q->data[i].num);
            if (i == q->rear)
                break;
        } while (i != q->front);
    }
    printf("\n");
}

// 삽입 함수
void add_rear(DequeType *q, element item)
{
    if (is_full(q))
        error("큐가 포화상태입니다");
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = item;
}

void add_front(DequeType *q, element val)

{
    if (is_full(q))
        error("큐가 포화상태입니다");
    q->data[q->front] = val;
    q->front = (q->front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
}

element delete_front(DequeType *q)
{
    if (is_empty(q))
        error("큐가 공백상태입니다");
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    return q->data[q->front];
}

element delete_rear(DequeType *q)
{
    int prev = q->rear;
    if (is_empty(q))
        error("큐가 공백상태입니다");
    q->rear = (q->rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
    return q->data[prev];
}

element get_front(DequeType *q)
{
    if (is_empty(q))
        error("큐가 공백상태입니다");
    return q->data[(q->front + 1) % MAX_QUEUE_SIZE];
}

element get_rear(DequeType *q)
{
    if (is_empty(q))
        error("큐가 공백상태입니다");
    return q->data[q->rear];
}
//========과제=============//

int main(void)
{
    DequeType queue;
    element song;
    int command;
    int num;
    int time;
    int totaltime = 0;

    init_deque(&queue);

    printf("--데이터 추가 단계--\n");

    while (is_full(&queue) && totaltime <= 30)
    {
        printf("예약(1) 노래부르기(2) 우선예약(3) : ");
        scanf_s("&d", &command);
        fflush(stdin);

        if (command == 1)
        {
            printf("노래 번호 : ");
            scanf_s("%d", &num);
            fflush(stdin);
            printf("노래 시간 : ");
            scanf_s("%d", &time);
            fflush(stdin);

            song.num = num;
            song.time = time;

            add_rear(&queue, song);

            printf("노래 예약 = ");
            deque_print(&queue);
        }
        else if (command == 2)
        {
            element now = delete_front(&queue);
            if (now.time == -1)
                continue;
            totaltime += now.time;
            printf("=== %d번 노래 부름(남은 시간 %d분)\n", now.num, 30 - totaltime);
        }
        else if (command == 3)
        {
            printf("노래 번호 : ");
            scanf_s("%d", &num);
            fflush(stdin);
            printf("노래 시간 : ");
            scanf_s("%d", &time);
            fflush(stdin);

            song.num = num;
            song.time = time;

            add_front(&queue, song);

            printf("노래 예약 = ");
            deque_print(&queue);
        }
        else
        {
            printf("입력 오류\n");
        }
    }

    printf("노래방 시간 종료\n");
    printf("남은 노래 = ");
    deque_print(&queue);

    return 0;
}