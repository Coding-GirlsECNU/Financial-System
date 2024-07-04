from ..sqlconfig import SessionLocal, engine
from ..model import Chart


def get_all_charts():
    session = SessionLocal()
    return session.query(Chart).all()


def save_chart(chart: dict):
    session = SessionLocal()
    chart = Chart(**chart)
    session.add(chart)
    session.commit()
    session.refresh(chart)
    return chart


def delete_chart(chart_id: int):
    try:
        session = SessionLocal()
        session.query(Chart).filter(Chart.chartid == chart_id).delete()
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False
