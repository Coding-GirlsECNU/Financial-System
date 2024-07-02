from sqlalchemy.orm import Session
from ..model import Dashboard
from typing import List
from ..schemas import Dashboard as DashboardSchema


def get_all_dashboard(db: Session) -> List[Dashboard] | None:
    try:
        res = db.query(Dashboard).all()
    except Exception as e:
        return None
    return res


def save_dashboard(db: Session, payload: DashboardSchema) -> Dashboard | None:
    dashboard = Dashboard(**payload.__dict__)
    try:
        db.add(dashboard)
        db.commit()
    except Exception as e:
        return None
    return dashboard


def delete_dashboard(db: Session, payload: DashboardSchema) -> bool:
    try:
        db.query(Dashboard).filter(Dashboard.dashboardid == payload.dashboardid).delete()
        db.commit()
    except Exception as e:
        return False
    return True
